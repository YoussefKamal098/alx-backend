# 0x01. Caching

## Table of Contents

1. [Project Overview](#project-overview)
2. [Background Context](#background-context)
3. [Learning Objectives](#learning-objectives)
4. [Resources](#resources)
5. [Project Requirements](#project-requirements)
6. [Implementation Details](#implementation-details)
7. [Caching Strategies](#caching-strategies)
    - [1. FIFO (First-In First-Out)](#1-fifo-first-in-first-out)
    - [2. LIFO (Last-In First-Out)](#2-lifo-last-in-first-out)
    - [3. LFU (Least Frequently Used)](#3-lfu-least-frequently-used)
    - [4. MRU (Most Recently Used)](#4-mru-most-recently-used)
    - [5. LRU (Least Recently Used)](#5-lru-least-recently-used)
8. [Using `OrderedDict`](#using-ordereddict)
9. [Testing](#testing)
10. [Final Notes](#final-notes)

## Project Overview

This project introduces caching systems and explores various caching algorithms to optimize data retrieval. Through hands-on implementation, we study the behaviors and efficiency of multiple cache replacement policies and understand the purpose and limitations of caching. Implementing caching mechanisms such as FIFO, LIFO, LRU, MRU, and LFU provides practical insights into memory management strategies, often used in software design for enhancing performance in data-heavy applications.

## Background Context

Caching is a critical concept in software development, particularly in applications that require fast data access and minimal latency. This project examines different caching algorithms and evaluates their use cases, strengths, and limitations. By the end of this project, you’ll understand how these algorithms impact caching efficiency and memory usage.

## Learning Objectives

By completing this project, you will be able to:

- Define what a caching system is and explain its purpose.
- Describe cache replacement policies:
  - FIFO (First-In, First-Out)
  - LIFO (Last-In, First-Out)
  - LRU (Least Recently Used)
  - MRU (Most Recently Used)
  - LFU (Least Frequently Used)
- Understand the limitations and constraints of caching systems.

## Resources

To support your understanding, you may refer to the following resources:

- **Cache Replacement Policies**:
  - [FIFO (First-In, First-Out)](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_(FIFO))
  - [LIFO (Last-In, First-Out)](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_(LIFO))
  - [LRU (Least Recently Used)](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU))
  - [MRU (Most Recently Used)](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_(MRU))
  - [LFU (Least Frequently Used)](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Frequently_Used_(LFU))

## Project Requirements

- All Python files must be compatible with **Ubuntu 18.04 LTS** and written for **Python 3.7**.
- Code should adhere to **Pycodestyle style** (version 2.5).
- Ensure all scripts are executable and have proper documentation:
  - **Modules**, **classes**, and **functions** should include a docstring explaining their purpose.
- Use the `BaseCaching` class provided in `base_caching.py` as the parent class for all caching classes implemented.

## Implementation Details

The `BaseCaching` class serves as the foundation for all caching classes in this project. The caching classes must inherit from `BaseCaching` and implement two primary methods:

- **put(self, key, item)**: Adds an item to the cache.
- **get(self, key)**: Retrieves an item from the cache by key.

### `BaseCaching` Class Example

```python
#!/usr/bin/python3
""" BaseCaching module """

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize the cache storage """
        self.cache_data = {}

    def print_cache(self):
        """ Print the current cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key """
        raise NotImplementedError("get must be implemented in your cache class")
```

### Docstring Standards

Each function and class in this project should include clear docstrings explaining the functionality and parameters.

#### Example Docstring for `put` method:

```python
def put(self, key, item):
    """
    Adds an item to the cache.
    
    If the cache exceeds `MAX_ITEMS`, an item must be removed based on the caching
    algorithm implemented in the derived class.

    Args:
        key (str): The key under which the item is stored.
        item (Any): The item to store in the cache.
    """
```

#### Example Docstring for `get` method:

```python
def get(self, key):
    """
    Retrieves an item from the cache by its key.

    Args:
        key (str): The key associated with the item to retrieve.

    Returns:
        Any: The cached item if found; otherwise, None.
    """
```

## Caching Strategies

Here’s a breakdown of how each caching strategy handles item **reinsertion** (when an item already in the cache is inserted again). Each strategy treats reinsertion differently based on its core principles:

| **Strategy**     | **Insert Behavior**                                                    | **Remove Behavior**                                                                            | **Reinsert Behavior**                                                                                                                                      | **Use Case** |
|------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **FIFO**         | Items are added to the end of the cache.                                | Removes the oldest item (first inserted) when the cache is full.                               | No position change on reinsertion; keeps the original insertion order.                                                                                     | Retains longest-used items until capacity is reached. |
| **LIFO**         | Items are added to the end of the cache; reinserting updates the last position. | Removes the most recent item (last inserted) when the cache is full.                           | Moves the item to the end (most recent position) when reinserted, effectively treating it as a new item.                                                  | Refreshes recent data frequently, retaining older items longer. |
| **LFU**          | Items are added with an access counter that increments each access.      | Removes the least frequently accessed item; if counts match, the oldest by insertion is removed. | Increases the access count on reinsertion without moving its position, reflecting higher priority but retaining time order if counts are the same.        | Ideal for data accessed often; prioritizes commonly used items. |
| **MRU**          | Items are added to the end, with the most recent access updating its position. | Removes the most recently accessed item when the cache is full.                                | Moves the item to the end when reinserted, marking it as "most recently used" and reprioritizing it in the cache.                                          | Good for caching patterns where most recent access indicates temporary or short-lived usage. |
| **LRU**          | Items are added normally, moving the accessed item to "most recent."    | Removes the least recently accessed item when the cache is full.                               | Moves the item to the end on reinsertion, making it the "most recently used," giving it higher priority in cache retention.                                | Great for scenarios where frequently accessed items remain needed. |


## Using `OrderedDict`

`OrderedDict` is a specialized dictionary in Python's `collections` module that maintains the order of items as they are added. This property is essential for implementing various caching strategies effectively. Below, we will explore some of the key methods of `OrderedDict` that are particularly relevant to caching, along with the data structures and algorithms used in its implementation.

### Data Structures in `OrderedDict`

Internally, `OrderedDict` is implemented using two main data structures:

1. **Doubly Linked List**:
   - `OrderedDict` maintains a doubly linked list of the entries (key-value pairs). Each entry contains pointers to both the previous and next entries. This allows for efficient insertion, deletion, and traversal of items while preserving their order.
   - The use of a doubly linked list ensures that when an item is accessed or modified, it can be quickly moved to the front or back of the list as needed.

2. **Hash Table**:
   - Alongside the doubly linked list, `OrderedDict` uses a hash table (or dictionary) to map keys to their corresponding nodes in the linked list. This enables fast access to items by key.
   - The hash table allows for average-case O(1) time complexity for lookups, insertions, and deletions, while the linked list ensures that the order of items is maintained.

### Key Methods of `OrderedDict`

1. **`move_to_end(key, last=True)`**:
   - This method moves the specified key to either the end (if `last=True`) or the beginning (if `last=False`) of the `OrderedDict`.
   - **Use in Caching**:
     - In strategies like LRU and MRU, this method is critical for updating the position of an item to reflect its recent access. When an item is accessed (or reinserted), it can be moved to the end of the dictionary to indicate that it was the most recently used.

   **Example**:
   ```python
   from collections import OrderedDict

   cache = OrderedDict()
   cache['A'] = 1
   cache['B'] = 2
   cache.move_to_end('A')  # Moves 'A' to the end
   ```

2. **`popitem(last=True)`**:
   - This method removes and returns a key-value pair from the `OrderedDict`. If `last=True`, it removes the last item; if `last=False`, it removes the first item.
   - **Use in Caching**:
     - This method is useful for removing items when the cache exceeds its capacity. Depending on the caching strategy, it can remove the oldest item (FIFO), the most recent (LIFO), or the least recently used (LRU).

   **Example**:
   ```python
   item = cache.popitem(last=False)  # Removes the first inserted item
   ```

3. **`__setitem__(key, value)`**:
   - This method is used to insert or update a key-value pair in the `OrderedDict`.
   - **Use in Caching**:
     - When inserting a new item or updating an existing item, this method can implicitly handle reinsertion. For example, if the item already exists, it is updated and moved to the end to signify that it has been recently accessed.

   **Example**:
   ```python
   cache['C'] = 3  # Adds a new item
   cache['A'] = 10  # Updates 'A' and moves it to the end
   ```

4. **`__delitem__(key)`**:
   - This method allows you to delete a specific key from the `OrderedDict`.
   - **Use in Caching**:
     - This can be used for explicitly removing items when certain conditions are met, such as when an item is evicted due to cache limits or when an item needs to be cleared from the cache for any reason.

   **Example**:
   ```python
   del cache['B']  # Removes 'B' from the cache
   ```

### Reinserting Items

When an item is reinserted into the `OrderedDict`, the following happens depending on the caching strategy:

- **FIFO**: The order remains the same; reinserted items do not affect their position.
- **LIFO**: The item moves to the end, marking it as the most recent.
- **LFU**: The access count increases, but the position does not change, maintaining the frequency order.
- **MRU**: The item moves to the end to mark it as recently used.
- **LRU**: The item moves to the end, updating its status to the most recently accessed.


## Testing

Ensure to conduct tests for each caching strategy implemented to verify:

- Correctness of data retrieval.
- Proper cache size limitations.
- Correct removal behavior based on the chosen strategy.

To execute a docstring containing test cases (like the one I've provided) from a `.txt` file in Python, you can use the `doctest` module. The example you've provided uses a Fish shell script to run Python's `doctest` against a Python module. Here's how you can set it up and run it step-by-step.

### Step 1: Save Your Docstring as a Text File
First, ensure that your docstring tests are saved in a `.txt` file. For example, you could name it `test_lfu_cache.txt`.

### Step 2: Create Your LFUCache Implementation
Ensure that you have the implementation of your `LFUCache` class in a Python file, e.g., `100-lfu_cache.py`.

### Step 3: Running the Tests Using Python
You can run your doctests directly from the command line or from a Python script. Below are both methods.

#### Method 1: From the Command Line
Using the Fish shell script you've provided, you can run the tests in your terminal. Ensure you are in the directory where your `test_lfu_cache.txt` and `100-lfu_cache.py` files are located.

1. Open your terminal and create a Fish shell script file, e.g., `run_tests.fish`:

    ```fish
    #!/usr/bin/env fish
    python3 -m doctest -v (basename (status -f))
    exit
    ```

2. Make the script executable:

    ```bash
    chmod +x run_tests.fish
    ```

3. Run the script:

    ```bash
    ./run_tests.fish test_lfu_cache.txt
    ```

#### Method 2: From a Python Script
Alternatively, you can create a Python script to run the tests directly. Create a new Python file, e.g., `run_tests.py`, with the following code:

```python
import doctest

# Specify the filename of your test file
filename = 'test_lfu_cache.txt'

# Run doctests
doctest.testfile(filename, module_relative=False, globs={'LFUCache': __import__('100-lfu_cache').LFUCache}, optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
```

### Step 4: Run Your Python Script
After creating the `run_tests.py` file, run it in the terminal:

```bash
python3 run_tests.py
```

### Key Points
- **Ensure the Import Works**: In the `doctest.testfile` function, make sure that the import path for `LFUCache` is correct and matches your project's structure.
- **Doctest Options**: The `optionflags` argument can be customized based on your needs. The example uses `doctest.REPORT_ONLY_FIRST_FAILURE` to stop at the first failure for easier debugging.

### Example of a Full Test Setup

1. **`100-lfu_cache.py`**:
    ```python
    class LFUCache:
        # Your LFUCache implementation here...
        pass
    ```

2. **`test_lfu_cache.txt`**:
    ```python
    """
    >>> LFUCache = __import__('100-lfu_cache').LFUCache
    >>> my_cache = LFUCache()
    >>> my_cache.put("A", "Hello")
    >>> my_cache.put("B", "World")
    >>> my_cache.put("C", "Holberton")
    >>> my_cache.put("D", "School")
    >>> my_cache.print_cache()
    Current cache:
    A: Hello
    B: World
    C: Holberton
    D: School

    >>> print(my_cache.get("B"))
    World
    ...
    """
    ```

3. **`run_tests.py`**:
    ```python
    import doctest

    # Specify the filename of your test file
    filename = 'test_lfu_cache.txt'

    # Run doctests
    doctest.testfile(filename, module_relative=False, globs={'LFUCache': __import__('100-lfu_cache').LFUCache}, optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    ```


Example test case scenarios could include adding items beyond capacity, retrieving non-existent keys, and verifying that items are removed according to the caching strategy.

## Final Notes

The goal of this project is not only to implement different caching strategies but also to understand the implications of using these strategies in real-world applications. By the end of this project, you should have a comprehensive understanding of caching principles and their practical applications in software design.


