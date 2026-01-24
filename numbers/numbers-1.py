#      Integers, floats, math operations, rounding, math & random modules
# Basic operations with numbers in Python

# Integer and float types
int_num = 11
float_num = 10.5
print("Integer:", int_num)
print("Float:", float_num)

# Basic arithmetic operations
sum_result = int_num + float_num
diff_result = float_num - int_num
prod_result = int_num * float_num
div_result = float_num / int_num
floor_div_result = float_num // int_num
mod_result = int_num % 4    # Remainder of division
exp_result = int_num ** 2

print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Division:", div_result)
print("Floor Division:", floor_div_result)
print("Modulo:", mod_result)
print("Exponentiation:", exp_result)

# Rounding numbers
rounded_num = round(float_num)
print("Rounded float:", rounded_num)    
# Rounding to 1 decimal place
rounded_num_1dp = round(float_num, 1)
print("Rounded float to 1 decimal place:", rounded_num_1dp) 




