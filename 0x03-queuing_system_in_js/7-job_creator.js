const kue = require('kue');

// Array of job data
const jobs = [
    { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
    { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
    { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account' },
    { phoneNumber: '4153538781', message: 'This is the code 4562 to verify your account' },
    { phoneNumber: '4153118782', message: 'This is the code 4321 to verify your account' },
    { phoneNumber: '4153718781', message: 'This is the code 4562 to verify your account' },
    { phoneNumber: '4159518782', message: 'This is the code 4321 to verify your account' },
    { phoneNumber: '4158718781', message: 'This is the code 4562 to verify your account' },
    { phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' },
    { phoneNumber: '4154318781', message: 'This is the code 4562 to verify your account' },
    { phoneNumber: '4151218782', message: 'This is the code 4321 to verify your account' },
];

// Create the queue
const queue = kue.createQueue();

// Create jobs in the queue
jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_2', jobData);

    // Log job creation
    job
        .on('enqueue', () => console.log(`Notification job created: ${job.id}`))
        .on('complete', () => console.log(`Notification job ${job.id} completed`))
        .on('failed', (error) => console.log(`Notification job ${job.id} failed: ${error}`))
        .on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`));

    // Save the job
    job.save((error) => {
        if (error) {
            console.log(`Failed to create notification job: ${error}`);
        }
    });
});
