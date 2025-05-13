# Implementing Heap Sort and Counting Sort
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr

# Example usage:
arr = [4, 10, 3, 5, 1]
print(heap_sort(arr))  # Output: [1, 3, 4, 5, 10]


# Countining Sort 
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

# Example usage:
arr = [1, 4, 1, 2, 7, 5, 2]
print(counting_sort(arr))  # Output: [1, 1, 2, 2, 4, 5, 7]
