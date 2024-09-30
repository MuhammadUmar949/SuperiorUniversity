import math


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

while True:
    user_input = input("Enter a number to check if it's prime (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        print("Exiting program.")
        break
    
    try:
        number = int(user_input)
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")
