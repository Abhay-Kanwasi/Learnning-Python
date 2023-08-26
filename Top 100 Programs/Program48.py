# Get the first digit of the number

number = 234#input("Enter the number : ")

# Method 1
# first_digit = str(number)[0]

# Method 2
# while number>=10:
#     number = number // 10
# print(number)

# Get the last digit of the number 

# Method 1
first = number % 10 
print(first)

# Method 2
while number >=10:
    number = number % 10
print(number)