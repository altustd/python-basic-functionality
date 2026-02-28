# Python basic functionality: loops
# Created by Troy Altus on 2/28/2026

# for loop
for i in range(5):
    print(i)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1  

# nested loops
for i in range(3):
    for j in range(2):
        print(f'i: {i}, j: {j}')    
# break statement
for i in range(10):
    if i == 5:
        break
    print(i)    

# continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)        

# else statement with loops
for i in range(5):
    print(i)    
else:
    print("Loop completed without break")

# infinite loop (commented out to prevent execution)
# while True:
#     print("This will run forever")

# Loop control with functions
def count_up_to(n):
    count = 0
    while count < n:
        print(count)
        count += 1  
count_up_to(5)  

# Looping through a list
my_list = ['apple', 'banana', 'cherry']
for fruit in my_list:
    print(fruit)


# Looping through a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key, value in my_dict.items():
    print(f'{key}: {value}')    

# Looping through a string
my_string = "Hello" 
for char in my_string:
    print(char) 

# Looping with enumerate
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(f'Index: {index}, Value: {value}')    

# Looping with zip
list1 = [1, 2, 3]
list2 = ['one', 'two', 'three']
for num, word in zip(list1, list2):
    print(f'Number: {num}, Word: {word}')   

# Looping with list comprehension
squares = [x**2 for x in range(10)]     
print(squares)  

# Looping with generator expression
squares_gen = (x**2 for x in range(10)) 
for square in squares_gen:
    print(square)   

# Looping with a function and a loop
def print_squares(n):
    for i in range(n):
        print(i**2)     
print_squares(5)        

# Looping with a while loop and a function
def count_down(n):
    while n > 0:
        print(n)
        n -= 1      
count_down(5)           

# Looping with a for loop and a function        
def print_cubes(n):
    for i in range(n):
        print(i**3)     
print_cubes(5)      

# Looping with a for loop and a list
my_list = [1, 2, 3, 4, 5]           
for num in my_list:
    print(num**2)   

# Looping with a while loop and a list
my_list = [1, 2, 3, 4, 5]       
index = 0
while index < len(my_list):
    print(my_list[index]**2)
    index += 1      

# Looping with a for loop and a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():      
    print(f'{key}: {value**2}')             

# Looping with a while loop and a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = list(my_dict.keys())                 
index = 0
while index < len(keys):
    key = keys[index]
    value = my_dict[key]
    print(f'{key}: {value**2}')
    index += 1      

# Looping with a for loop and a string
my_string = "Hello, World!"     
for char in my_string:
    print(char) 

# Looping with a while loop and a string
my_string = "Hello, World!"
index = 0       
while index < len(my_string):
    print(my_string[index])
    index += 1  

# Looping with a for loop and a set
my_set = {1, 2, 3, 4, 5}    
for num in my_set:
    print(num**2)       

# Looping with a while loop and a set
my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
index = 0   
while index < len(my_list):
    print(my_list[index]**2)
    index += 1  

# Looping with a for loop and a tuple
my_tuple = (1, 2, 3, 4, 5)  
for num in my_tuple:
    print(num**2)           

# Looping with a while loop and a tuple
my_tuple = (1, 2, 3, 4, 5)
index = 0
while index < len(my_tuple):
    print(my_tuple[index]**2)
    index += 1      

# Looping with a for loop and a range
for num in range(10):
    print(num**2)           

# Looping with a while loop and a range
num = 0         
while num < 10:
    print(num**2)
    num += 1        

# Looping with a for loop and a list comprehension
squares = [x**2 for x in range(10)] 
print(squares)      

# Looping with a while loop and a list comprehension
squares = []        
num = 0
while num < 10:
    squares.append(num**2)
    num += 1
print(squares)  

# Looping with a for loop and a generator expression
squares_gen = (x**2 for x in range(10))         
for square in squares_gen:
    print(square)   

# Looping with a while loop and a generator expression
squares_gen = (x**2 for x in range(10))
while True:
    try:
        square = next(squares_gen)
        print(square)
    except StopIteration:
        break  

# Looping with a for loop and a function that returns a generator
def generate_squares(n):        
    for i in range(n):
        yield i**2      
squares_gen = generate_squares(10)
for square in squares_gen:
    print(square)       

# Looping with a while loop and a function that returns a generator
def generate_squares(n):        
    for i in range(n):
        yield i**2
squares_gen = generate_squares(10)
while True:             
    try:
        square = next(squares_gen)
        print(square)
    except StopIteration:
        break       

# Looping with a for loop and a function that returns a list
def generate_squares(n):
    return [i**2 for i in range(n)]     
squares = generate_squares(10)  
for square in squares:
    print(square)   

# Looping with a while loop and a function that returns a list
def generate_squares(n):
    return [i**2 for i in range(n)]
squares = generate_squares(10)          
index = 0
while index < len(squares):     
    print(squares[index])
    index += 1          



