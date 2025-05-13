# Finding the K Smallest and K Largest Elements Using a Heap
import heapq

def find_k_smallest(arr, k):
    return heapq.nsmallest(k, arr)

def find_k_largest(arr, k):
    return heapq.nlargest(k, arr)

# Example usage:
arr = [10, 4, 3, 20, 15, 7]
print(find_k_smallest(arr, 3))  # Output: [3, 4, 7]
print(find_k_largest(arr, 2))   # Output: [20, 15]
