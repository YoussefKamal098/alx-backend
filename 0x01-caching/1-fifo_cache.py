#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def is_full(self):
        """Checks if the cache is full.
        """
        return len(self.cache_data) >= BaseCaching.MAX_ITEMS

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return

        if self.is_full() and key not in self.cache_data:
            last_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", last_key)

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
