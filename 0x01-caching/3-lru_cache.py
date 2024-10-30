#!/usr/bin/env python3
"""Least Recently Used caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with an LRU
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
            least_recent_access_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", least_recent_access_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)

        return self.cache_data.get(key, None)
