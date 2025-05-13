# Understand and compare the time complexity of different algorithms.
import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time

def main():
    random_list = [random.randint(1, 10000) for _ in range(1000)]

    bubble_time = measure_time(bubble_sort, random_list)
    merge_time = measure_time(merge_sort, random_list)
    quick_time = measure_time(quick_sort, random_list)

    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    print(f"Quick Sort Time: {quick_time:.6f} seconds")

    algorithms = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
    times = [bubble_time, merge_time, quick_time]

    plt.bar(algorithms, times, color=['red', 'blue', 'green'])
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Execution Time Comparison')
    plt.show()

if __name__ == "__main__":
    main()
    
# RESULTS =  SO as we run our code we can see that the bubble sort is the slowest algorithm, while the quick sort is the fastest. The merge sort is in between.
# Fastest: Quick Sort > Merge Sort > Bubble Sort