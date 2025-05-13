#  LRU Cache Implementation
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    
    def display(self):
        print("LRU Cache:", self.cache)

# Test
cache = LRUCache(2)
cache.put(1, "A")
cache.put(2, "B")
print("Get 1:", cache.get(1))  # A
cache.put(3, "C")  # Evicts key 2
print("Get 2:", cache.get(2))  # -1
cache.display()