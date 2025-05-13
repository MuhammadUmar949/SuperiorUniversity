# Implementing a Priority Queue Using a Heap
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value, priority):
        heapq.heappush(self.queue, (priority, value))

    def dequeue(self):
        if not self.queue:
            return None
        return heapq.heappop(self.queue)[1]

    def peek(self):
        if not self.queue:
            return None
        return self.queue[0][1]

# Example usage:
pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)
print(pq.dequeue())  # Output: "Task B" (highest priority)
