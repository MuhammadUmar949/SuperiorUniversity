# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Loop Detection and Removal
def detect_and_remove_loop(head):
    slow = fast = head
    loop_exists = False
    
    # Detect loop using Floyd's algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_exists = True
            break
    
    if not loop_exists:
        return False
    
    # Find the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    # Find the last node of the loop
    while fast.next != slow:
        fast = fast.next
    
    # Remove the loop
    fast.next = None
    return True

# Test case
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Creates a loop

print("Before removal:")
print("Loop exists:", detect_and_remove_loop(node1))
print("After removal:")
print("Loop exists:", detect_and_remove_loop(node1))