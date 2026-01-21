# Sets: unordered, mutable collections of unique elements in Python 
# Basic operations and methods  

# Creating a set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print("Initial set:", my_set)   

# Adding an element to the set
my_set.add(13)
print("After adding 13:", my_set)   

# Removing an element from the set
my_set.remove(5)
print("After removing 5:", my_set)  

# Discarding an element from the set (no error if not present)
my_set.discard(20)  # 20 is not in the set
print("After discarding 20 (not present):", my_set) 

# Popping an arbitrary element from the set
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("Set after popping an element:", my_set)

# Clearing all elements from the set
my_set.clear()
print("Set after clearing all elements:", my_set)       

