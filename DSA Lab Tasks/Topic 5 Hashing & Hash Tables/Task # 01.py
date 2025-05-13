#  Hash Table with Collision Handling
class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                self.table[hash_key][i] = (key, value)
                return
        self.table[hash_key].append((key, value))
    
    def get(self, key):
        hash_key = self._hash(key)
        for k, v in self.table[hash_key]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                del self.table[hash_key][i]
                return
        raise KeyError(key)
    
    def display(self):
        for i in range(self.size):
            print(f"{i}: {self.table[i]}")

class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.keys = [None] * size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_key = self._hash(key)
        for i in range(self.size):
            index = (hash_key + i) % self.size
            if self.keys[index] is None or self.keys[index] == key:
                self.table[index] = value
                self.keys[index] = key
                return
        raise Exception("Hash table is full")
    
    def get(self, key):
        hash_key = self._hash(key)
        for i in range(self.size):
            index = (hash_key + i) % self.size
            if self.keys[index] == key:
                return self.table[index]
            if self.keys[index] is None:
                break
        return None
    
    def delete(self, key):
        hash_key = self._hash(key)
        for i in range(self.size):
            index = (hash_key + i) % self.size
            if self.keys[index] == key:
                self.table[index] = None
                self.keys[index] = None
                # Rehash all keys in the cluster
                next_index = (index + 1) % self.size
                while self.keys[next_index] is not None:
                    k, v = self.keys[next_index], self.table[next_index]
                    self.keys[next_index] = None
                    self.table[next_index] = None
                    self.insert(k, v)
                    next_index = (next_index + 1) % self.size
                return
            if self.keys[index] is None:
                break
        raise KeyError(key)
    
    def display(self):
        for i in range(self.size):
            print(f"{i}: {self.keys[i]} => {self.table[i]}")