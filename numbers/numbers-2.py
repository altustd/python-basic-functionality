# Integers, floats, math operations, rounding, math & random modules
# Basic operations with numbers in Python

# Using math module
import math
import random

# Math module functions
sqrt_result = math.sqrt(16)
ceil_result = math.ceil(10.3)
floor_result = math.floor(10.7)
factorial_result = math.factorial(5)        
print("Square root of 16:", sqrt_result)
print("Ceiling of 10.3:", ceil_result)
print("Floor of 10.7:", floor_result)
print("Factorial of 5:", factorial_result)

# Using random module
random_float = random.random()  # Random float between 0.0 and 1.
random_int = random.randint(1, 100)  # Random integer between 1 and 100
random_choice = random.choice(['apple', 'banana', 'cherry'])  # Random choice from a list
print("Random float between 0.0 and 1.0:", random_float)
print("Random integer between 1 and 100:", random_int)
print("Random choice from list:", random_choice)

# Generating a random sample from a range
random_sample = random.sample(range(1, 101), 5)  # 5 unique random numbers from 1 to 100
print("Random sample of 5 unique numbers from 1 to 100:", random_sample)    

# Rounding numbers
rounded_number = round(10.756, 2)  # Round to 2 decimal places
print("Rounded number:", rounded_number)    

# Rounding to nearest integer
rounded_integer = round(10.756)
print("Rounded integer:", rounded_integer)  

# Rounding to 1 decimal place
rounded_one_decimal = round(10.756, 1)
print("Rounded to 1 decimal place:", rounded_one_decimal)       

# Rounding to nearest ten
rounded_ten = round(10.756, -1)  # Round to nearest ten (i.e., to the nearest 10)
print("Rounded to nearest ten:", rounded_ten)   

# Rounding to nearest hundred
rounded_hundred = round(10.756, -2)  # Round to nearest hundred (i.e., to the nearest 100)
print("Rounded to nearest hundred:", rounded_hundred)       

# Rounding to nearest thousand
rounded_thousand = round(10.756, -3)  # Round to nearest thousand (i.e., to the nearest 1000)
print("Rounded to nearest thousand:", rounded_thousand)         

# Generating random integers in a specific range
random_range_int = random.randint(50, 150)  # Random integer between 50 and 150
print("Random integer between 50 and 150:", random_range_int)       

# Generating random float in a specific range
random_range_float = random.uniform(50.0, 150.0)  # Random float between 50.0 and 150.0
print("Random float between 50.0 and 150.0:", random_range_float)           

# Generating a random choice from a tuple
random_tuple_choice = random.choice((10, 20, 30, 40, 50))
print("Random choice from tuple:", random_tuple_choice)     

# Generating a random sample from a list
random_list_sample = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)  # 3 unique random numbers from the list
print("Random sample of 3 unique numbers from the list:", random_list_sample)   


# # Generating a random sample from a set
# random_set_sample = random.sample({11, 22, 33, 44, 55}, 2)  # 2 unique random numbers from the set
# print("Random sample of 2 unique numbers from the set:", random_set_sample) 
# This will raise an error:
# TypeError: Population must be a sequence.  For dicts or sets, use sorted(d)

# Generating a random sample from a string
random_string_sample = random.sample("abcdefghij", 4)  # 4 unique random characters from the string
print("Random sample of 4 unique characters from the string:", random_string_sample)       

# Generating a random sample from a range with step
random_range_step_sample = random.sample(range(0, 101, 10), 5)  # 5 unique random numbers from 0 to 100 with step of 10 
print("Random sample of 5 unique numbers from range 0 to 100 with step 10:", random_range_step_sample)       

# Generating a random sample from a large range
random_large_range_sample = random.sample(range(1, 10001), 10)  # 10 unique random numbers from 1 to 10000
print("Random sample of 10 unique numbers from 1 to 10000:", random_large_range_sample)       

# Generating a random sample from a range of negative numbers
random_negative_range_sample = random.sample(range(-100, 0), 5)  # 5 unique random numbers from -100 to -1
print("Random sample of 5 unique numbers from -100 to -1:", random_negative_range_sample)       

# Generating a random sample from a range of floating point numbers
random_float_range_sample = random.sample([i * 0.1 for i in range(1, 101)], 5)  # 5 unique random floats from 0.1 to 10.0
print("Random sample of 5 unique floats from 0.1 to 10.0:", random_float_range_sample)       

# Generating a random sample from a range of even numbers
random_even_range_sample = random.sample(range(2, 201, 2), 5)  # 5 unique random even numbers from 2 to 200
print("Random sample of 5 unique even numbers from 2 to 200:", random_even_range_sample)       

# Generating a random sample from a range of odd numbers
random_odd_range_sample = random.sample(range(1, 201, 2), 5)  # 5 unique random odd numbers from 1 to 200
print("Random sample of 5 unique odd numbers from 1 to 200:", random_odd_range_sample)       

