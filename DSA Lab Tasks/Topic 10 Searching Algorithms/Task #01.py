# inear and Binary Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Test
arr = [10, 23, 45, 70, 11, 15]
sorted_arr = sorted(arr)
print("Linear search (45):", linear_search(arr, 45))
print("Binary search (45):", binary_search(sorted_arr, 45))