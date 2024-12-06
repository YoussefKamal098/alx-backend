const { promisify } = require('util');
const redis = require('redis');

// Create a Redis client
const client = redis.createClient({
    host: 'localhost',
    port: 6379
});

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});


// Function to set a new school with a value
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print); // Use redis.print to display confirmation message
}

// Function to display a school's value
async function displaySchoolValue(schoolName) {
    console.log(await promisify(client.get).bind(client)(schoolName));
}

async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
    console.log('Redis client connected to the server');
    await main();
});
