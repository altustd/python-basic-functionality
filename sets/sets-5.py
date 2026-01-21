# Sets are unordered, mutable collections of unique elements in Python.
# Basic operations and methods  

setA = {1, 2, 3, 4, 5, 7, 8, 9}
print("Original Set A:", setA)      
setB = {1, 2,3 , 10, 11, 12} 
print("Original Set B:", setB)

# Symmetric Difference Update is used to update a set with the symmetric difference of itself and another set.
# It removes elements that are common to both sets and adds elements that are unique to each set.

setA.symmetric_difference_update(setB)
print("Set A after symmetric_difference_update with Set B:", setA)




