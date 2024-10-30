#!/usr/bin/env python3
"""Least Frequently Used caching module.
"""
from collections import OrderedDict, defaultdict
from base_caching import BaseCaching
from typing import Any, Hashable, Optional


class Node:
    """Represents a node in the LFU Cache."""

    def __init__(self, item: Any, frequency: int = 1):
        self.item = item
        self.frequency = frequency

    def __str__(self):
        return f"{self.item}"


class LFUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LFU
    removal mechanism when the limit is reached.
    """

    def __init__(self) -> None:
        """Initializes the cache.
        """
        super().__init__()

        # Map from frequency to keys with that frequency
        self.freq_map: defaultdict[int, OrderedDict[Hashable, Node]] = \
            defaultdict(OrderedDict)
        self.min_freq: int = 0  # Track the minimum frequency

    def is_full(self) -> bool:
        """Checks if the cache is full.
        """
        return len(self.cache_data) >= BaseCaching.MAX_ITEMS

    def _remove_key(self, key: Hashable, freq: int) -> None:
        """Remove a key from the frequency map."""
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:  # If no keys at this frequency, remove it
            del self.freq_map[freq]
            self._update_min_freq(freq)

    def _update_min_freq(self, freq: int) -> None:
        """Update min_freq if necessary."""
        if self.min_freq == freq:
            self.min_freq += 1

    def _update_freq(self, key: Hashable) -> None:
        """Update the frequency of the key."""
        current_node = self.cache_data[key]
        current_freq = current_node.frequency

        # Remove the key from its current frequency list
        self._remove_key(key, current_freq)

        # Increment the frequency and update the node
        new_freq = current_freq + 1
        current_node.frequency = new_freq
        self.freq_map[new_freq][key] = current_node

    def put(self, key: Hashable, item: Any) -> None:
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Key exists, update its item and frequency
            self.cache_data[key].item = item
            self._update_freq(key)
            return

        if self.is_full():
            self._evict_lfu_key()

        # Insert the new key with a Node containing the item and frequency 1
        self.cache_data[key] = Node(item)
        self.freq_map[1][key] = self.cache_data[key]
        self.min_freq = 1  # Reset min_freq to 1

    def _evict_lfu_key(self) -> None:
        """Evict the least frequently used key from the cache."""
        least_freq_key, _ = self.freq_map[self.min_freq].popitem(last=False)
        print("DISCARD:", least_freq_key)
        del self.cache_data[least_freq_key]

    def get(self, key: Hashable) -> Optional[Any]:
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self._update_freq(key)
            return self.cache_data[key].item  # Return the item from the node

        return None  # Return None if key is not found
