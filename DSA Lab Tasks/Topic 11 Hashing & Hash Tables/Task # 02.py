# Custom Hash Function
def custom_hash(key, table_size):
    hash_val = 0
    for char in str(key):
        hash_val = (hash_val * 31 + ord(char)) % table_size
    return hash_val

def analyze_hash_function(hash_func, data, table_size):
    distribution = [0] * table_size
    collisions = 0
    
    for item in data:
        hash_val = hash_func(item, table_size)
        if distribution[hash_val] > 0:
            collisions += 1
        distribution[hash_val] += 1
    
    print(f"Collisions: {collisions}")
    print(f"Distribution: {distribution}")
    return distribution

# Test
data = ["hello", "world", "python", "algorithm", "data", "structure"]
print("Custom hash analysis:")
analyze_hash_function(custom_hash, data, 10)
print("\nBuilt-in hash analysis:")
analyze_hash_function(lambda k, s: hash(k) % s, data, 10)