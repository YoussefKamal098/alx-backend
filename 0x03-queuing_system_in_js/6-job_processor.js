const kue = require('kue');

// Create the queue
const queue = kue.createQueue();

// Define the sendNotification function
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process the queue
queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;

    // Call sendNotification with job data
    sendNotification(phoneNumber, message);

    // Mark the job as done
    done();
});
