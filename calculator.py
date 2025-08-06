# Step 1: Ask the user to input the first number
num1 = int(input("Enter the first number:"))
# Step 2: Ask the user to input the second number
num2 = int(input("Enter the second number:"))

# Step 3: Compute the Sum,Difference,Product and Quotient.
# Add the two numbers.
sum_result = num1 + num2

# Subtract the two numbers
difference_result = num1 - num2

# Multiply the two numbers
product_result = num1 * num2

# Divide the first number by the second number
quotient_result = num1 / num2

# Step 4: Print the result
print(f"Results of the two numbers:")
print(f"Sum:{sum_result:}")
print(f"Difference:{difference_result:}")
print(f"Product:{product_result:}")
print(f"Quotient:{quotient_result:}")