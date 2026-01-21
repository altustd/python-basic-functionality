# Strings are sequences of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# They are immutable, meaning they cannot be changed after creation.

greeting = "Hello, World!"
print("Original string:", greeting) 

# Looping through each character in the string
for char in greeting:
    print(char)

# Checking for character membership
if 'H' in greeting:
    print("'H' is present in the string.")
if 'z' in greeting:
    print("'z' is present in the string.")
else:
    print("'z' is not present in the string.")  

# Check for substrings  
if "World" in greeting:
    print("'World' is a substring of the string.")
if "Python" in greeting:
    print("'Python' is a substring of the string.")
else:
    print("'Python' is not a substring of the string.")     



