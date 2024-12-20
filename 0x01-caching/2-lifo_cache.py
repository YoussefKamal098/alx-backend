#!/usr/bin/env python3
"""Last-In First-Out caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
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
            last_inserted_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", last_inserted_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
