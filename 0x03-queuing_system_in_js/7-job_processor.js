const kue = require('kue');

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create the queue
const queue = kue.createQueue();

// Define the notification function
function sendNotification(phoneNumber, message, job, done) {
    // Set initial progress
    job.progress(0, 100);

    if (blacklistedNumbers.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // Midway progress
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // Complete the job
    done();
}

// Process the queue
queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
