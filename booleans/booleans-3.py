# Random Boolean Values and Operations
import random   

# Generating random boolean values
random_bool1 = random.choice([True, False]) # Randomly choose True or False
random_bool2 = random.choice([True, False]) # Randomly choose True or False
print("Random boolean 1:", random_bool1)
print("Random boolean 2:", random_bool2) 

# Combining random boolean values
print("Random boolean 1 and Random boolean 2:", random_bool1 and random_bool2)
print("Random boolean 1 or Random boolean 2:", random_bool1 or random_bool2)
print("not Random boolean 1:", not random_bool1)     