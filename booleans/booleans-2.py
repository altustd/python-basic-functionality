#  More Boolean Operations and Comparisons 
#  Combining logical and comparison operators    
x = 15
y = 25
z = 15
print("x < y and x == z:", x < y and x == z)
print("x > y or x == z:", x > y or x == z)
print("not (x != z):", not (x != z))    

# Chained comparisons
print("1 < 2 < 3:", 1 < 2 < 3)
print("1 < 2 > 3:", 1 < 2 > 3)  
print("3 > 2 >= 2:", 3 > 2 >= 2)
print("3 < 2 <= 2:", 3 < 2 <= 2)    

# Identity operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]       
print("list1 is list2:", list1 is list2)  # True
print("list1 is list3:", list1 is list3)  # False
print("list1 is not list3:", list1 is not list3)  # True        

# Membership operators
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)      # True
print("6 not in my_list:", 6 not in my_list)  # True    
print("10 in my_list:", 10 in my_list)    # False
print("0 not in my_list:", 0 not in my_list)  # True        

# Combining membership and logical operators
print("3 in my_list and 6 not in my_list:", 3 in my_list and 6 not in my_list)
print("10 in my_list or 0 not in my_list:", 10 in my_list or 0 not in my_list)
print("not (3 in my_list):", not (3 in my_list))    

# Boolean conversion
print("bool(1):", bool(1))          # True
print("bool(0):", bool(0))          # False
print("bool('Hello'):", bool("Hello"))  # True
print("bool(''):", bool(""))        # False
print("bool([1, 2, 3]):", bool([1, 2, 3]))  # True
print("bool([]):", bool([]))        # False 
print("bool(None):", bool(None))    # False 
print("bool({1: 'a'}):", bool({1: 'a'}))  # True
print("bool({}):", bool({}))        # False 

# Complex boolean expressions
print("not (True and False):", not (True and False))
print("not (True or False):", not (True or False))
print("not (False and True):", not (False and True))
print("not (False or True):", not (False or True))
print("(10 > 5) and (5 < 3):", (10 > 5) and (5 < 3))
print("(10 > 5) or (5 < 3):", (10 > 5) or (5 < 3))
print("not (10 == 10):", not (10 == 10))    # Combining multiple comparisons    
print("((3 < 5) and (5 < 10)) or (10 == 20):", ((3 < 5) and (5 < 10)) or (10 == 20))
print("((3 > 5) or (5 < 10)) and (10 != 20):", ((3 > 5) or (5 < 10)) and (10 != 20))        
  

