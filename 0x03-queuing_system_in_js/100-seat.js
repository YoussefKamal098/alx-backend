const express = require('express');
const redis = require('redis');
const { promisify }  = require('util');
const kue = require('kue');

const app = express();
const port = 1245;

// Redis Client
const client = redis.createClient();
client.on('error', (err) => console.error('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

// Promisify Redis commands
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Kue Queue
const queue = kue.createQueue();

// Global Variables
let reservationEnabled = true;

// Helper Functions
const reserveSeat = async (number) => {
    await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
    const seats = await getAsync('available_seats');
    return seats ? parseInt(seats, 10) : 0;
};

// Routes
app.get('/available_seats', async (req, res) => {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        res.json({ status: 'Reservation are blocked' });
        return;
    }

    const job = queue.create('reserve_seat').save((err) => {
        if (err) {
            res.json({ status: 'Reservation failed' });
            return;
        }
        res.json({ status: 'Reservation in process' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (errMessage) => {
        console.log(`Seat reservation job ${job.id} failed: ${errMessage}`);
    });
});

app.get('/process', (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        const availableSeats = await getCurrentAvailableSeats();

        if (availableSeats <= 0) {
            reservationEnabled = false;
            done(new Error('Not enough seats available'));
            return;
        }

        const newSeats = availableSeats - 1;
        await reserveSeat(newSeats);

        if (newSeats === 0) {
            reservationEnabled = false;
        }

        done();
    });
});

// Initialize available seats
reserveSeat(50).then(()=>{
    // Start server
    app.listen(port, () => {
        console.log(`Server listening on port ${port}`);
    });
}).catch((err) => {
    console.error('Reservation Error: ', err);
});
