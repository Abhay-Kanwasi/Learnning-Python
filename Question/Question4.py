# Add two numbers

# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# add = a + b
# print(f"Addition of {a} and {b} is {add}.")



# Subtract two numbers in python

# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# subtract = a - b
# print(f"Subtraction of {a} and {b} is {subtract}.")


# Product two numbers in Python

# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# product = a * b
# print(f"Product of {a} and {b} is {product}.")


# Division two number in python

# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# try:
#     divide = a / b
#     print(f"Product of {a} and {b} is {divide}.")
# except ZeroDivisionError:
#     print("Zero can't be a denominator.")


# Average of two numbers.

# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# avg = (a + b)/2
# print(f"Average of two number is : {avg}")


# Area of circle

# r = int(input("Enter the radius : "))
# pi = 3.14
# area_of_circle = pi*(r**2)
# print(f"Area of circle is {area_of_circle} of {r} radius.")


# Area of triangle

# b = int(input("Enter the bredth : "))
# h = int(input("Enter the height : "))
# area_of_triangle = 1/2*b*h
# print(f"Area of triangle is {area_of_triangle}")


# Area of rectangle

# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))
# area_of_rectangle = a*b
# print(f"Area of rectangle is {area_of_rectangle}")


# Swap two numbers in python

# temp = 0
# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))
# print(f"\nBefore swapping\nThe value of a : {a}\nThe value of b : {b}")
# temp = a
# a = b
# b = temp
# print(f"\nAfter swapping\nThe value of a : {a}\nThe value of b : {b}")


# Simple intrest in python

# p = float(input("Enter the principal : "))
# r = float(input("Enter the rate : "))
# t = float(input("Enter the time : "))
# simple_intrest = (p*r*t)/100
# print("Simple Intrest : ",simple_intrest)


# Compound intrest in python

principal = int(input("Enter the principal : "))
rate = int(input("Enter the rate : "))
time = int(input("Enter the time : "))
number = int(input("Enter the number : "))

rate = rate /100
amount = principal*pow(1+(rate/number),number*time)
ci = amount - principal

print("Compound intrest = ",ci)
print("Total amount = ",amount)