# Sets are unordered, mutable collections of unique elements in Python.
# Basic operations and methods  

myset = {1, 2, 3, 4, 5, 7, 8, 9}
print("Original set:", myset)

# Checking for membership in the set
if 3 in myset:
    print("yes, 3 is in the set")
if 6 in myset:
    print("yes, 6 is in the set")
else:
    print("no, 6 is not in the set")

# Adding an element to the set
myset.add(6)    
print("Set after adding 6:", myset)

# Removing an element from the set
myset.remove(3)
print("Set after removing 3:", myset)

# Demonstrating set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# Intersection
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

# Difference
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b (set_a - set_b):", difference_set)

# Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference of set_a and set_b:", symmetric_difference_set)











