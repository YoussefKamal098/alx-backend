const redis = require('redis');

// Create a Redis client
const client = redis.createClient({
    host: 'localhost',
    port: 6379
});

// Check connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});
