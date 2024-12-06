### **What is Kue?**

**Kue** is a job and task queue library for Node.js that uses Redis as a backend to store and manage jobs. It allows you to create, manage, and process background jobs in a reliable and efficient way. Kue is useful for scenarios where you need to perform tasks asynchronously, such as sending emails, processing images, or performing lengthy calculations, without blocking the main application thread.

### **Key Features of Kue**:

1. **Job Queueing**:
    - Kue allows you to add jobs to a queue with specific data. These jobs are then processed in the background by workers.

2. **Persistent Jobs**:
    - Jobs are stored in Redis, making them persistent even if the application crashes. This ensures that jobs are not lost and can be retried or processed later.

3. **Job Processing**:
    - Kue allows you to create worker processes that process jobs asynchronously. This helps offload resource-heavy tasks from the main application, improving performance and user experience.

4. **Job States**:
    - Kue has built-in support for job states such as "completed", "failed", "active", and "delayed". This helps you track the progress of each job and handle job retries or failures effectively.

5. **Priority and Delays**:
    - You can assign priority to jobs (e.g., low, medium, high) and set delays for jobs, which makes it easy to control the order and timing of job execution.

6. **Progress Tracking**:
    - Kue allows you to track the progress of each job, enabling you to report on or log how far a job has progressed.

7. **Job Events**:
    - Kue emits events when jobs are created, completed, or fail. You can hook into these events to execute custom logic (e.g., send a notification when a job completes).

8. **Job Retries**:
    - Kue supports automatic job retries in case of failure, so jobs can be re-attempted a specified number of times before being marked as failed.

### **Why Use Kue?**

1. **Asynchronous Task Processing**:
    - In many applications, certain tasks are not time-sensitive and can be executed in the background. Kue helps you offload these tasks to a separate process or worker, freeing up resources for real-time operations.

2. **Scaling**:
    - By using Kue with Redis, you can easily scale your job processing. You can add more worker processes to handle jobs in parallel, allowing the system to handle a high volume of tasks efficiently.

3. **Reliability and Persistence**:
    - Redis ensures that jobs are persisted even if the application crashes. This guarantees that jobs are not lost, and they can be retried when necessary.

4. **Separation of Concerns**:
    - By offloading certain tasks (like sending emails, generating reports, or processing payments) to background workers, you can keep the main application focused on handling user requests and interactions.

5. **Job Management**:
    - Kue provides an easy-to-use API for managing jobs. You can monitor job statuses, cancel jobs, or inspect job details. This gives you full control over how jobs are processed and allows you to build custom job management features.

6. **Error Handling and Retries**:
    - Kue's built-in error handling and retry mechanisms allow you to easily handle failures. If a job fails, Kue can retry it a specified number of times, ensuring reliability.

7. **Priority and Delays**:
    - You can prioritize jobs and delay their execution, allowing you to implement complex scheduling logic. For example, you might want to process critical jobs immediately and delay less important ones.

8. **Track Job Progress**:
    - With Kue, you can track the progress of long-running jobs and provide feedback to users. For example, if a job is processing a large file, you can report how much of the file has been processed.

### **When to Use Kue?**

Kue is best suited for tasks that:
- **Are time-consuming or resource-intensive** (e.g., sending emails, image processing, data aggregation).
- **Can be done asynchronously** (i.e., tasks that don’t need to block user interactions or real-time responses).
- **Need to be reliable** (i.e., jobs should not be lost if the application crashes).
- **Require retry logic** (e.g., retrying a failed job after a delay).
- **Benefit from background processing** (e.g., executing tasks outside of the main application flow).

### **Common Use Cases**:

1. **Email Notifications**:
    - Sending transactional emails (like registration confirmation or password reset) asynchronously, ensuring fast responses for users.

2. **Image Processing**:
    - Resizing images, compressing them, or performing other transformations can be done in the background, so users can continue interacting with the app without delays.

3. **Reporting and Data Aggregation**:
    - Long-running tasks like generating reports or aggregating large datasets can be handled asynchronously, preventing the main app from getting bogged down.

4. **Video Transcoding**:
    - Video transcoding is a resource-heavy task that can be queued for background processing, allowing the app to respond quickly to users while the video is being processed.

5. **Social Media Sharing**:
    - Posting content to social media or external systems can be offloaded to a background job queue, improving the user experience by reducing delays.

6. **Processing Payments**:
    - Payment processing tasks, such as validating transactions or updating records, can be done in the background without blocking the user interface.

### **Kue vs Other Queueing Systems**:

Kue is great for simple use cases in Node.js and works well with Redis, but if you need more advanced features or more complex workflows, you might consider alternatives such as:
- **Bull**: A more feature-rich job queue that also uses Redis, with features like rate limiting, job prioritization, job scheduling, and more.
- **Bee-Queue**: Another Redis-backed queue, designed to be simpler and faster, with fewer features than Kue but ideal for high-throughput scenarios.
- **RabbitMQ**: A more complex, full-featured messaging queue that is language-agnostic and supports advanced routing, pub/sub, and message acknowledgement.

### **Summary**:

Kue is a simple, lightweight, and reliable job queue library for Node.js that leverages Redis to store and process jobs asynchronously. It is useful for handling time-consuming tasks in the background, improving the responsiveness of your application. Kue provides job states, event listeners, priority, and retries, making it a powerful tool for building scalable and fault-tolerant systems that need background task processing.

---

Here is a comprehensive guide on **Kue** with examples for all its key features.

### **1. Setting Up Kue**:

Before diving into examples, let’s first set up Kue. First, ensure you have Redis running locally and install Kue:

```bash
npm install kue
```

Now, you can start using Kue in your project.

### **2. Job Queueing with Kue**:

The core of Kue is job queueing. Here's an example of how to add a job to a queue.

```js
const kue = require('kue');
const queue = kue.createQueue();

// Create a job
const job = queue.create('email', {
  to: 'user@example.com',
  subject: 'Welcome!',
  body: 'Thank you for signing up!'
}).save((err) => {
  if (err) {
    console.log('Error creating job:', err);
  } else {
    console.log(`Job created: ${job.id}`);
  }
});
```

This code creates a job in a queue named `email` with the data provided. The job is saved to Redis.

### **3. Job Processing**:

Once a job is added to the queue, you need to create a worker that processes it. Here's an example worker that processes the job:

```js
queue.process('email', (job, done) => {
  console.log(`Sending email to: ${job.data.to}`);
  // Simulate sending email
  setTimeout(() => {
    console.log(`Email sent to ${job.data.to} with subject: ${job.data.subject}`);
    done(); // Job is completed
  }, 1000);
});
```

This worker processes the email job, simulates sending the email, and then calls `done()` to mark the job as complete.

### **4. Job States**:

Kue supports various job states like `completed`, `failed`, `active`, etc. You can listen to job events to track the state of a job.

```js
queue.process('email', (job, done) => {
  console.log(`Sending email to: ${job.data.to}`);
  setTimeout(() => {
    done(); // Mark job as complete
  }, 1000);
});

// Listen for job events
queue.on('job complete', (id, result) => {
  console.log(`Job ${id} completed successfully.`);
});

queue.on('job failed', (id, err) => {
  console.log(`Job ${id} failed with error: ${err}`);
});
```

In this example:
- When a job is completed, the `job complete` event is triggered.
- When a job fails, the `job failed` event is triggered.

### **5. Job Priority**:

You can set priorities for jobs to control which jobs should be processed first. The higher the priority, the sooner the job will be processed.

```js
queue.create('email', { to: 'user@example.com', subject: 'High priority email' })
  .priority('high') // Set high priority
  .save();

queue.create('email', { to: 'user@example.com', subject: 'Low priority email' })
  .priority('low')  // Set low priority
  .save();
```

Jobs with higher priority will be processed before jobs with lower priority.

### **6. Job Delays**:

You can delay the execution of a job by specifying a delay in milliseconds.

```js
queue.create('email', {
  to: 'user@example.com',
  subject: 'Delayed email',
  body: 'This email is delayed.'
})
.delay(5000)  // Delay the job for 5 seconds
.save();
```

This job will be delayed by 5 seconds before it gets processed.

### **7. Job Progress**:

You can track the progress of a job by updating its progress during execution.

```js
queue.process('email', (job, done) => {
  let progress = 0;
  let interval = setInterval(() => {
    progress += 10;
    job.progress(progress, 100);
    if (progress === 100) {
      clearInterval(interval);
      done(); // Job completed
    }
  }, 500);
});
```

In this example, the job progress is updated every 500ms until it reaches 100%, and then the job is marked as completed.

### **8. Job Retries**:

Kue supports automatic job retries in case of failure. You can set how many times a job should be retried if it fails.

```js
queue.create('email', { to: 'user@example.com', subject: 'Retry email' })
  .attempts(3)  // Retry 3 times if job fails
  .save();
```

If the job fails, Kue will retry it up to 3 times before marking it as failed.

### **9. Job Events**:

You can hook into job events such as `job complete`, `job failed`, `job progress`, etc. This allows you to execute custom logic whenever a job changes its state.

```js
queue.on('job complete', (id, result) => {
  console.log(`Job ${id} completed successfully.`);
});

queue.on('job failed', (id, err) => {
  console.log(`Job ${id} failed with error: ${err}`);
});
```

### **10. Delayed Jobs**:

You can also delay the execution of jobs by specifying a delay in milliseconds.

```js
queue.create('email', {
  to: 'user@example.com',
  subject: 'Delayed email'
}).delay(2000).save();
```

This will delay the job for 2 seconds before it is processed.

### **11. Removing Jobs**:

You can remove a job from the queue if it’s no longer needed.

```js
queue.create('email', { to: 'user@example.com', subject: 'Remove email' })
  .save((err, job) => {
    if (err) {
      console.log('Error creating job:', err);
    } else {
      console.log(`Job created: ${job.id}`);
      // Remove job after creation
      job.remove();
    }
  });
```

### **12. Graceful Shutdown**:

When you want to shut down your application, you can gracefully stop the queue and workers:

```js
queue.shutdown(5000, (err) => {
  console.log('Queue shut down.');
});
```

This will stop the queue and workers after finishing all active jobs, giving them up to 5 seconds to finish before shutting down.

---

### **Example Summary**:

```js
const kue = require('kue');
const queue = kue.createQueue();

// Create a job with priority and delay
const job = queue.create('email', {
  to: 'user@example.com',
  subject: 'Welcome to Kue!',
  body: 'This email is sent in the background.'
})
.priority('high')  // Set priority
.delay(3000)       // Delay by 3 seconds
.attempts(5)       // Retry job 5 times if it fails
.save((err) => {
  if (err) {
    console.log('Error creating job:', err);
  } else {
    console.log(`Job created with ID: ${job.id}`);
  }
});

// Process the email job
queue.process('email', (job, done) => {
  console.log(`Sending email to: ${job.data.to}`);
  setTimeout(() => {
    console.log(`Email sent to ${job.data.to} with subject: ${job.data.subject}`);
    done();
  }, 1000);
});

// Listen for job events
queue.on('job complete', (id, result) => {
  console.log(`Job ${id} completed successfully.`);
});

queue.on('job failed', (id, err) => {
  console.log(`Job ${id} failed with error: ${err}`);
});

queue.on('job progress', (id, progress, total) => {
  console.log(`Job ${id} is ${progress}% complete`);
});
```

### **Conclusion**:

Kue provides an easy-to-use and feature-rich solution for job queueing in Node.js applications. It handles job states, retries, priorities, and more. Whether you're handling background tasks like email sending or long-running computations, Kue can help you scale and manage these tasks asynchronously and reliably.