# Dynamic Array Implementation
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.length = 0
        self.array = self._make_array(self.capacity)
    
    def _make_array(self, size):
        return [None] * size
    
    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    
    def append(self, item):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.length] = item
        self.length += 1
    
    def insert(self, index, item):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = item
        self.length += 1
    
    def delete(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        for i in range(index, self.length-1):
            self.array[i] = self.array[i+1]
        self.length -= 1
        if self.length < self.capacity // 4:
            self._resize(self.capacity // 2)
    
    def search(self, item):
        for i in range(self.length):
            if self.array[i] == item:
                return i
        return -1
    
    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.array[index]
    
    def __len__(self):
        return self.length
    
    def __repr__(self):
        return str(self.array[:self.length])