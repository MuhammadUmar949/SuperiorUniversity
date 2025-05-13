#  Hash Table with Collision Handling
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(key)
    
    def display(self):
        for i in range(self.size):
            print(f"{i}: {self.table[i]}")

# Test
ht = HashTable(10)
ht.insert("name", "Alice")
ht.insert("age", 25)
print("Get name:", ht.get("name"))
ht.delete("age")
print("Get age after delete:", ht.get("age"))