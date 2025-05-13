# Stack Implementations
# Array-based stack
class ArrayStack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Linked list-based stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.is_empty():
            item = self.top.data
            self.top = self.top.next
            return item
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.top.data
        raise IndexError("Peek from empty stack")
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count