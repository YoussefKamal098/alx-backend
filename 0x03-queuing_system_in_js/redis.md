Redis provides a versatile data structure and command set for storing, manipulating, and managing data. Here's a detailed breakdown of operations for single values, hashes, sets, and arrays (lists), including expiration control, along with examples using Node.js.

---

## **Redis Operations Overview**

### **1. Single Values**
- Single values are simple `key-value` pairs, where the value is a string.

#### **Common Operations**
| Operation          | Command/Method in Redis | Example (Node.js using `redis` package) |
|---------------------|--------------------------|-----------------------------------------|
| **Set Value**       | `SET key value`         | `client.set('username', 'john')`        |
| **Get Value**       | `GET key`               | `client.get('username')`               |
| **Delete Key**      | `DEL key`               | `client.del('username')`               |
| **Check Key Exists**| `EXISTS key`            | `client.exists('username')`            |
| **Set Expiration**  | `SET key value EX time` | `client.set('username', 'john', 'EX', 10)` |

#### **Example: Single Value Operations**
```js
const redis = require('redis');
const client = redis.createClient();

client.set('username', 'john', 'EX', 10, (err, reply) => {
  if (err) console.error(err);
  else console.log(reply); // OK
});

client.get('username', (err, value) => {
  if (err) console.error(err);
  else console.log(value); // john
});
```

---

### **2. Hashes**
- Hashes store a mapping of fields to values, like a dictionary or object.

#### **Common Operations**
| Operation          | Command/Method in Redis       | Example (Node.js using `redis`)       |
|---------------------|-------------------------------|---------------------------------------|
| **Set Field**       | `HSET key field value`        | `client.hset('user', 'name', 'Alice')`|
| **Get Field**       | `HGET key field`             | `client.hget('user', 'name')`        |
| **Get All Fields**  | `HGETALL key`                | `client.hgetall('user')`             |
| **Delete Field**    | `HDEL key field`             | `client.hdel('user', 'name')`        |
| **Set Expiration**  | `EXPIRE key time`            | `client.expire('user', 10)`          |

#### **Example: Hash Operations**
```js
client.hset('user', 'name', 'Alice', (err, reply) => {
  if (err) console.error(err);
  else console.log(reply); // 1 (number of fields added)
});

client.hget('user', 'name', (err, value) => {
  if (err) console.error(err);
  else console.log(value); // Alice
});

client.hgetall('user', (err, hash) => {
  if (err) console.error(err);
  else console.log(hash); // { name: 'Alice' }
});
```

---

### **3. Sets**
- Sets are unordered collections of unique values.

#### **Common Operations**
| Operation           | Command/Method in Redis | Example (Node.js using `redis`)     |
|----------------------|--------------------------|-------------------------------------|
| **Add Member**       | `SADD key value`        | `client.sadd('colors', 'red')`     |
| **Remove Member**    | `SREM key value`        | `client.srem('colors', 'red')`     |
| **Get All Members**  | `SMEMBERS key`          | `client.smembers('colors')`        |
| **Check Membership** | `SISMEMBER key value`   | `client.sismember('colors', 'red')`|
| **Set Expiration**   | `EXPIRE key time`       | `client.expire('colors', 10)`      |

#### **Example: Set Operations**
```js
client.sadd('colors', 'red', 'blue', 'green', (err, reply) => {
  if (err) console.error(err);
  else console.log(reply); // 3 (number of elements added)
});

client.smembers('colors', (err, members) => {
  if (err) console.error(err);
  else console.log(members); // ['red', 'blue', 'green']
});
```

---

### **4. Arrays (Lists)**
- Lists are ordered collections of strings, similar to arrays.

#### **Common Operations**
| Operation            | Command/Method in Redis | Example (Node.js using `redis`)   |
|-----------------------|--------------------------|-----------------------------------|
| **Push to Front**     | `LPUSH key value`       | `client.lpush('tasks', 'task1')` |
| **Push to Back**      | `RPUSH key value`       | `client.rpush('tasks', 'task2')` |
| **Pop from Front**    | `LPOP key`              | `client.lpop('tasks')`           |
| **Pop from Back**     | `RPOP key`              | `client.rpop('tasks')`           |
| **Get Range**         | `LRANGE key start end`  | `client.lrange('tasks', 0, -1)`  |
| **Set Expiration**    | `EXPIRE key time`       | `client.expire('tasks', 10)`     |

#### **Example: List Operations**
```js
client.rpush('queue', 'task1', 'task2', (err, reply) => {
  if (err) console.error(err);
  else console.log(reply); // 2 (number of items in list)
});

client.lrange('queue', 0, -1, (err, items) => {
  if (err) console.error(err);
  else console.log(items); // ['task1', 'task2']
});
```

---

### **5. Expiration and Key Management**
- Redis supports setting expiration for any key, regardless of its type.
- Expired keys are automatically removed by Redis.

#### **Setting Expiration**
```js
// Set expiration (10 seconds)
client.set('tempKey', 'value', 'EX', 10, (err, reply) => {
  if (err) console.error(err);
  else console.log(reply); // OK
});

// Check expiration time (TTL)
client.ttl('tempKey', (err, ttl) => {
  if (err) console.error(err);
  else console.log(ttl); // Time-to-live in seconds
});

// Delete key manually
client.del('tempKey', (err, reply) => {
  if (err) console.error(err);
  else console.log(reply); // 1 (number of keys deleted)
});
```

---

### **6. Checking Key Existence**
- Use `EXISTS key` to check if a key exists.

#### **Example**
```js
client.exists('username', (err, exists) => {
  if (err) console.error(err);
  else console.log(exists); // 1 if exists, 0 otherwise
});
```

---

### **7. Deleting Keys**
- Use `DEL key` to delete a key explicitly.

#### **Example**
```js
client.del('username', (err, reply) => {
  if (err) console.error(err);
  else console.log(reply); // 1 if the key was deleted, 0 otherwise
});
```

---

### **Conclusion**
Redis operations are versatile and allow for the efficient storage and manipulation of single values, hashes, sets, and arrays. The `redis` package in Node.js provides an easy interface to interact with Redis. By combining these operations with expiration, key management, and atomic commands, Redis becomes a powerful tool for caching, messaging, and data manipulation in distributed systems.