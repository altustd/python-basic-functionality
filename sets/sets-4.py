# Sets are unordered, mutable collections of unique elements in Python.
# Basic operations and methods  

setA = {1, 2, 3, 4, 5, 7, 8, 9}
print("Original Set A:", setA)      
setB = {1,2,3,10,11,12} 
print("Original Set B:", setB)

setA.difference_update(setB)
print("Set A after difference_update with Set B:", setA)


