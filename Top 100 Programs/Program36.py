# Swapping two numbers without third variable

a = int(input("Enter a number :"))
b = int(input("Enter a number :"))

# Using Addition & Subtraction

# a = a + b # We add both numbers and store it in one of the numbers. now a contains the addition of a and b.
# b = a - b
# a = a - b

# print("The value of a :",a)
# print("The value of b :",b)

# Using Multiplication & Division

a = a * b
b = a / b
a = a / b

print("The value of a :",a)
print("The value of b :",b)