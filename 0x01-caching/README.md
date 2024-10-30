# 0x01. Caching

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

## Testing

Testing and verifying the caching behavior can be done by running the scripts with `npm run dev` for JavaScript-based projects or directly executing the Python files. Logs should be checked for the expected caching behavior and eviction as per the cache policies.

## Final Notes

This project’s completion will give you a deep understanding of caching policies and prepare you for implementing efficient caching mechanisms in real-world applications.
