# Boolean logic, comparison operators, truthy/falsy values  

# Boolean values
bool_true = True
bool_false = False
print("Boolean True:", bool_true)
print("Boolean False:", bool_false)     

# Logical operators
a = True
b = False
print("a and b:", a and b)  # Logical AND
print("a or b:", a or b)    # Logical OR
print("not a:", not a)      # Logical NOT       

# Comparison operators
a = 10
b = 20
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a < b:", a < b)    # Less than
print("a <= b:", a <= b)  # Less than or equal to
print("a > b:", a > b)    # Greater than
print("a >= b:", a >= b)  # Greater than or equal to        

# Truthy and Falsy values
truthy_values = [1, "non-empty string", [1, 2, 3], (1,), {1: 'a'}]
falsy_values = [0, "", [], (), {}, None]    
for value in truthy_values:
    if value:
        print(f"{value} is truthy")
for value in falsy_values:
    if not value:
        print(f"{value} is falsy")  

