const redis = require('redis');
const client = redis.createClient();

// Check connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

// Delete the existing key to avoid type conflict
client.del('ALX', (err, reply) => {
    if (err) {
        console.error('Error deleting key ALX:', err);
    } else {
        console.log('Deleted key ALX:', reply);
    }

    // Store the hash values using HSET
    client.hset('ALX', 'Portland', 50, redis.print);
    client.hset('ALX', 'Seattle', 80, redis.print);
    client.hset('ALX', 'New York', 20, redis.print);
    client.hset('ALX', 'Bogota', 20, redis.print);
    client.hset('ALX', 'Cali', 40, redis.print);
    client.hset('ALX', 'Paris', 2, redis.print);

    // Retrieve and display the entire hash using HGETALL
    client.hgetall('ALX', (err, reply) => {
        if (err) {
            console.error('Error retrieving hash:', err);
        } else {
            console.log(reply); // Displays the entire hash
        }
    });
});
