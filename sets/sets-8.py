# Sets: unordered, mutable collections of unique elements in Python.
# Frozensets: immutable versions of sets.

a = frozenset([1, 2, 3, 4, 5, 6])
print("Original Set a:", a)
# Checking for membership in the frozenset
if 3 in a:
    print("yes, 3 is in the frozenset a")
if 9 in a:      
    print("yes, 9 is in the frozenset a")
else:
    print("no, 9 is not in the frozenset a")

# Attempting to add an element to the frozenset (will raise an AttributeError)
try:
    a.add(7)
except AttributeError as e:
    print("Error:", e)

# Attempting to remove an element from the frozenset (will raise an AttributeError)
try:
    a.remove(2)
except AttributeError as e:
    print("Error:", e)  



