#! /usr/bin/evn python
import datetime


class DCache(object):

    def __init__(self):
        self._cache = {}
        self._max_cache_size = 10

    def __contains__(self, key):
        return key in self._cache

    def update(self, key, value):
        # if cache has reached max, flush old entries
        if key not in self._cache and len(self._cache) >= self._max_cache_size:
            self.remove_oldest()

        self._cache[key] = {'date_accessed': datetime.datetime.now(),
                            'value': value}

    def remove_oldest(self):
        oldest_entry = None
        for key in self._cache:
            if not oldest_entry:
                oldest_entry = key
            elif (self._cache[key]['date_accessed'] <
                  self._cache[oldest_entry]['date_access']):
                oldest_entry = key

        self._cache.pop(oldest_entry)

    @property
    def size(self):
        return len(self._cache)
