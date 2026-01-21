# Sets are unordered, mutable collections of unique elements in Python.
# Basic operations and methods  

setA = {1, 2, 3, 4, 5, 6}
print("Original Set A:", setA)      
setB = {1, 2, 3} 
print("Original Set B:", setB)

# A subset is a set where all elements of the first set are also in the second set.
# A superset is a set that contains all elements of another set.
# Disjoint sets are sets that have no elements in common.


setA.issubset(setB)
print("Is Set B a subset of Set A?", setB.issubset(setA))   

setA.issuperset(setB)
print("Is Set A a superset of Set B?", setA.issuperset(setB))   

setA.isdisjoint(setB)
print("Are Set A and Set B disjoint?", setA.isdisjoint(setB))   







