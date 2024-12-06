const kue = require('kue');

// Create the queue named push_notification_code
const queue = kue.createQueue();

// Create the job data object
const jobData = {
    phoneNumber: '+1234567890',
    message: 'Your code is 123456'
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData)
    .save((err) => {
        if (err) {
            console.log('Error creating job:', err);
        } else {
            console.log(`Notification job created: ${job.id}`);
        }
    });

// Listen for job completion
job.on('complete', () => {
    console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', (errorMessage) => {
    console.log('Notification job failed:', errorMessage);
});
