# Integers, floats, math operations, rounding, math & random modules
# Basic operations with numbers in Python

# Using math module
import math
import random

# Generating a random sample from a range of prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
prime_numbers = [i for i in range(2, 201) if is_prime(i)]
random_prime_range_sample = random.sample(prime_numbers, 5)  # 5 unique random prime numbers from 2 to 200
print("Random sample of 5 unique prime numbers from 2 to 200:", random_prime_range_sample)      

# Generating a random sample from a range of multiples of 5
random_multiples_of_5_sample = random.sample(range(5, 501, 5), 5)  # 5 unique random multiples of 5 from 5 to 500
print("Random sample of 5 unique multiples of 5 from 5 to 500:", random_multiples_of_5_sample)       

# Generating a random sample from a range of squares of numbers
squares = [i**2 for i in range(1, 32)]  # Squares of numbers from 1 to 31
random_squares_sample = random.sample(squares, 5)  # 5 unique random squares
print("Random sample of 5 unique squares from 1^2 to 31^2:", random_squares_sample)       

# Generating a random sample from a range of cubes of numbers
cubes = [i**3 for i in range(1, 22)]  # Cubes of numbers from 1 to 21
random_cubes_sample = random.sample(cubes, 5)  # 5 unique random cubes
print("Random sample of 5 unique cubes from 1^3 to 21^3:", random_cubes_sample)       

# Generating a random sample from a range of Fibonacci numbers
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
fib_numbers = fibonacci(20)  # First 20 Fibonacci numbers
random_fib_sample = random.sample(fib_numbers, 5)  # 5 unique random Fibonacci numbers
print("Random sample of 5 unique Fibonacci numbers from first 20:", random_fib_sample)      

