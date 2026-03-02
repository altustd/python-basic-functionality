# Lists in Python

# A list is a collection of items that are ordered and changeable (mutable). 
# - One of the most commonly used data structures in Python and can be used to store a variety of data types, including integers, floats, strings, and even other lists.
# - Defined by enclosing the items in square brackets []
# - Can contain items of different types, including other lists


my_list = [1, 2, 3, 4, 5]
print(my_list)  


# List methods
# 1. append() - Adds an item to the end of the list
my_list.append(6)   
print(my_list)  

# 2. insert() - Inserts an item at a specified position
my_list.insert(0, 0)    
print(my_list)     

# 3. remove() - Removes the first occurrence of a specified item
my_list.remove(3)   
print(my_list)

# 4. pop() - Removes and returns the item at a specified position (default is the last item)
popped_item = my_list.pop() 
print(popped_item)
print(my_list)  

# 5. sort() - Sorts the items of the list in ascending order
my_list.sort()      
print(my_list) 

# 6. reverse() - Reverses the order of the items in the list
my_list.reverse()   
print(my_list)  

# 7. count() - Returns the number of occurrences of a specified item
count_of_2 = my_list.count(2)   
print(count_of_2)

# 8. index() - Returns the index of the first occurrence of a specified item    
index_of_4 = my_list.index(4)
print(index_of_4)

# 9. clear() - Removes all items from the list
my_list.clear()
print(my_list)  

# 10. copy() - Returns a shallow copy of the list
new_list = my_list.copy()
print(new_list) 

# 11. extend() - Adds the elements of another list to the end of the current list
my_list.extend([7, 8, 9])
print(my_list)

# 12. len() - Returns the number of items in the list
length_of_list = len(my_list)   
print(length_of_list)     

