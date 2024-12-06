const redis = require('redis');

// Create the Redis client
const publisher = redis.createClient();

// Handle connection event
publisher.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle error event
publisher.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to publish message after a delay
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        publisher.publish('ALXchannel', message);
    }, time);
}

// Publish messages with different delays
publishMessage("ALX Student #1 starts course", 100);
publishMessage("ALX Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("ALX Student #3 starts course", 400);
