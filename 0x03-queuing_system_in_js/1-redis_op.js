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


// Function to set a new school with a value
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print); // Use redis.print to display confirmation message
}

// Function to display a school's value
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, result) => {
        if (err) {
            console.error('Error retrieving value:', err);
        } else {
            console.log(result); // Log the value of the school
        }
    });
}

// Execute the required operations
displaySchoolValue('ALX');  // Should log null or error if the key doesn't exist
setNewSchool('ALXSanFrancisco', '100'); // Set value for ALXSanFrancisco
displaySchoolValue('ALXSanFrancisco');  // Should log 100
