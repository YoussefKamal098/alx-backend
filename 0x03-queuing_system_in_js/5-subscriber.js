const redis = require('redis');

// Create the Redis client
const subscriber = redis.createClient();

// Handle connection event
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle error event
subscriber.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the ALXchannel
subscriber.subscribe('ALXchannel');

// Handle message event
subscriber.on('message', (channel, message) => {
    console.log(message);

    // If the message is KILL_SERVER, unsubscribe and quit
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe('ALXchannel');
        subscriber.quit();
    }
});
