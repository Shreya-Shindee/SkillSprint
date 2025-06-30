from functools import lru_cache
import json
import time
from typing import Dict, List

# In-memory cache with TTL
class ResourceCache:
    def __init__(self, ttl=3600):  # 1 hour TTL
        self.cache = {}
        self.ttl = ttl
    
    def get(self, key: str):
        if key in self.cache:
            data, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return data
            else:
                del self.cache[key]  # Remove expired
        return None
    
    def set(self, key: str, value):
        self.cache[key] = (value, time.time())

# Global cache instance
resource_cache = ResourceCache(ttl=1800)  # 30 minutes

@lru_cache(maxsize=128)
def get_cached_resources(skill_name: str):
    """LRU cache for frequently requested skills"""
    cached = resource_cache.get(skill_name)
    if cached:
        return cached
    
    # Expensive operation
    resources = search_resources_expensive(skill_name)
    resource_cache.set(skill_name, resources)
    return resources