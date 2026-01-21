# Sets are unordered, mutable collections of unique elements in Python.
# Basic operations and methods  

setA = {1, 2, 3, 4, 5, 6}
print("Original Set A:", setA)      

# setB = setA
# print("Set B (reference to Set A):", setB)
# setB.add(7)
# print("Set A after adding 7 to Set B:", setA)

setC = setA.copy()
print("Set C (copy of Set A):", setC)

setC.add(8)
print("Set A after adding 8 to Set C:", setA)
print("Set C after adding 8:", setC)
# Sets are unordered, mutable collections of unique elements in Python.
# They are defined using curly braces {} or the set() function. 

# Another way to create a set
setD = set(setA)    
print("Set D created using set(setA) function:", setD)
# Checking for membership in the set
if 4 in setD:
    print("yes, 4 is in Set D")
if 10 in setD:
    print("yes, 10 is in Set D")
else:
    print("no, 10 is not in Set D") 










