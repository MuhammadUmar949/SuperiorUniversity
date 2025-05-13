#  Exponential and Fibonacci Search
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    
    low = i // 2
    high = min(i, n-1)
    def binary_search(sub_arr, target):
        low, high = 0, len(sub_arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if sub_arr[mid] == target:
                return mid
            elif sub_arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    result = binary_search(arr[low:high+1], target)
    return result + low if result != -1 else -1

def fibonacci_search(arr, target):
    n = len(arr)
    fib2 = 0  # (m-2)th Fibonacci number
    fib1 = 1   # (m-1)th Fibonacci number
    fib = fib1 + fib2  # mth Fibonacci number
    
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    
    offset = -1
    
    while fib > 1:
        i = min(offset + fib2, n-1)
        
        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    
    if fib1 and arr[offset+1] == target:
        return offset+1
    return -1

# Test
arr = [2, 4, 8, 16, 32, 64, 128]
print("Exponential search (32):", exponential_search(arr, 32))
print("Fibonacci search (32):", fibonacci_search(arr, 32))