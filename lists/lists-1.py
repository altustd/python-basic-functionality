# Lists in Python

# A list is a collection of items that are ordered and changeable (mutable). 
# - One of the most commonly used data structures in Python and can be used to store a variety of data types, including integers, floats, strings, and even other lists.
# - Defined by enclosing the items in square brackets []
# - Can contain items of different types, including other lists



# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements in a list
print(my_list[0])  
print(my_list[2])  

# Modifying elements in a list
my_list[1] = 20 
print(my_list)  

# Adding elements to a list
my_list.append(6)       
print(my_list) 
my_list.insert(2, 15)
print(my_list)  

# Removing elements from a list
my_list.remove(20)
print(my_list)  
my_list.pop(2)  
print(my_list)

# List slicing
sliced_list = my_list[1:4]
print(sliced_list)  

# List concatenation
another_list = [7, 8, 9]
concatenated_list = my_list + another_list
print(concatenated_list)  

# List repetition               
repeated_list = my_list * 2
print(repeated_list)  

# Checking if an element is in a list
print(15 in my_list)         
print(10 in my_list)  

# Length of a list
print(len(my_list))  

# Iterating through a list
for item in my_list:
    print(item) 

# List comprehension
squared_list = [x**2 for x in my_list]  
print(squared_list) 

# Nested lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[0])  
print(nested_list[1][0])  

