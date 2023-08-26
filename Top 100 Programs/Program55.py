# Factorial of a number

number = int(input("Enter the number : "))

factorial = 1
for element in range(1,number+1):
    factorial = factorial * element
print(factorial)