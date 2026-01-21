# Strings are sequences of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# They are immutable, meaning they cannot be changed after creation.

my_string = "Hello, World!"
print("Original string:", my_string)

# Try changing a character (will raise an error because strings are immutable)
try:
    my_string[0] = 'h'
except TypeError as e:
    print("Error:", e)  

# Accessing characters in a string
first_char = my_string[0]
print("First character:", first_char)
last_char = my_string[-1]
print("Last character:", last_char)

# Slicing a string
substring = my_string[7:12]
print("Substring (7 to 12):", substring)
substring = my_string[:5]
print("Substring (start to 5):", substring)     
substring = my_string[7:]
print("Substring (7 to end):", substring)
substring = my_string[:]
print("Full string using slice:", substring)  
substring = my_string[::1]
print("Every character (step 1):", substring)    
substring = my_string[::2]
print("Every second character:", substring)
substring = my_string[::-1]
print("Reversed string:", substring)


# String methods
upper_string = my_string.upper()
print("Uppercase string:", upper_string)
lower_string = my_string.lower()
print("Lowercase string:", lower_string)
replaced_string = my_string.replace("World", "Python")
print("Replaced string:", replaced_string)
split_string = my_string.split(", ")
print("Split string:", split_string)

# String concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print("Full greeting:", full_greeting)

# String formatting
age = 30
formatted_string = f"{name} is {age} years old."
print("Formatted string:", formatted_string)    

# Escape sequences
escaped_string = "He said, \"It's a beautiful day!\"\nLet's enjoy it."
print("Escaped string:\n", escaped_string)  
# Multiline strings
multiline_string = """This is a multiline string.
It can span multiple lines.
Tabs and new lines are preserved."""
print("Multiline string:\n", multiline_string)  

# Raw strings (ignores escape sequences)
raw_string = r"C:\Users\Name\Documents\file.txt"
print("Raw string:", raw_string)  

# String membership testing
if "World" in my_string:
    print("yes, 'World' is in the string")
if "Python" in my_string:
    print("yes, 'Python' is in the string")
else:
    print("no, 'Python' is not in the string")  

# String length
string_length = len(my_string)
print("Length of the string:", string_length)




