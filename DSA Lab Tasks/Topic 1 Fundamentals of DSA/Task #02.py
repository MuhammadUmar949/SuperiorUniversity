#  Analyze and compare recursion with iteration in solving problems.
import time
import matplotlib.pyplot as plt
from functools import lru_cache

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    if n <= 1:
        return n
    else:
        return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    
def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time

def main():
    n_values = [10, 20, 30, 40]
    results = {
        'Recursive': [],
        'Iterative': [],
        'Memoized': []
    }
    
    for n in n_values:
        _, time_recursive = measure_time(fibonacci_recursive, n)
        results['Recursive'].append(time_recursive)
        
        _, time_iterative = measure_time(fibonacci_iterative, n)
        results['Iterative'].append(time_iterative)
        
        _, time_memoized = measure_time(fibonacci_memoized, n)
        results['Memoized'].append(time_memoized)
    
    plt.plot(n_values, results['Recursive'], label='Recursive')
    plt.plot(n_values, results['Iterative'], label='Iterative')
    plt.plot(n_values, results['Memoized'], label='Memoized')
    
    plt.xlabel('n')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Fibonacci Execution Time Comparison')
    plt.legend()
    plt.grid()
    plt.show()

    for n in n_values:
        print(f"n = {n}:")
        print(f"  Recursive: {results['Recursive'][n_values.index(n)]:.6f} seconds")
        print(f"  Iterative: {results['Iterative'][n_values.index(n)]:.6f} seconds")
        print(f"  Memoized: {results['Memoized'][n_values.index(n)]:.6f} seconds")
        print()

if __name__ == "__main__":
    main()
# RESULTS =  SO as we run our code we can see that the recursive approach is the slowest algorithm, while the iterative approach is the fastest. The memoized approach is in between.
