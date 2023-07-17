# Find the absolute number 

number = int(input("Enter the number : "))

# Solution 1
# print(f"The absolute value of {number} is",abs(number))

# Solution 2
if number <= 0:
    print(f"The absolute value of {number} is {number*-1}.")
else:
    print(f"The absolute value of {number} is {number*1}.")
