# Implementing a Min-Heap and Max-Heap
import heapq

class Heap:
    def __init__(self, heap_type="min"):
        self.heap_type = heap_type
        self.heap = []
    
    def insert(self, value):
        if self.heap_type == "min":
            heapq.heappush(self.heap, value)
        else:  # Max-Heap
            heapq.heappush(self.heap, -value)
    
    def extract_root(self):
        if not self.heap:
            return None
        if self.heap_type == "min":
            return heapq.heappop(self.heap)
        else:
            return -heapq.heappop(self.heap)
    
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0] if self.heap_type == "min" else -self.heap[0]
    
    def heapify(self, array):
        if self.heap_type == "min":
            self.heap = array
        else:
            self.heap = [-x for x in array]
        heapq.heapify(self.heap)

# Example usage:
min_heap = Heap("min")
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(2)
print(min_heap.extract_root())  # Output: 2

max_heap = Heap("max")
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(20)
max_heap.insert(2)
print(max_heap.extract_root())  # Output: 20
