""""Task 3: Visualizing Big-O Notation 
Objective: Develop an interactive Python program to visualize the growth of different time 
complexities. 
Instructions: 
1. Implement functions for different complexities (O(1), O(log n), O(n), O(n log n), 
O(n^2), O(2^n)). 
2. Generate input sizes from 1 to 1000 and compute the corresponding output values. 
3. Write a report explaining the meaning of these complexities and real-world examples 
of each. 
Deliverables: 
• Python script with complexity functions 
• Graphs comparing different complexities 
• A report explaining Big-O notation with examples"""

# Visualizing Big-O Notation
# Developing an interactive Python program to visualize the growth of different time complexities.

import matplotlib.pyplot as plt
import numpy as np
import math

def constant(n):
    return np.ones_like(n)

def log_n(n):
    return np.log2(n)

def linear(n):
    return n

def n_log_n(n):
    return n * np.log2(n)

def quadratic(n):
    return n ** 2

def exponential(n):
    return 2 ** n

n = np.arange(1, 1001) 
n_exp = np.arange(1, 21)

plt.figure(figsize=(12, 8))

plt.plot(n, constant(n), label='O(1)')
plt.plot(n, log_n(n), label='O(log n)')
plt.plot(n, linear(n), label='O(n)')
plt.plot(n, n_log_n(n), label='O(n log n)')
plt.plot(n, quadratic(n), label='O(n²)')
plt.plot(n_exp, exponential(n_exp), label='O(2ⁿ)')  

plt.title('Big-O Time Complexity Comparison')
plt.xlabel('Input Size (n)')
plt.ylabel('Operations (arbitrary units)')
plt.legend()
plt.grid(True)
plt.ylim(0, 100000)  
plt.show()
