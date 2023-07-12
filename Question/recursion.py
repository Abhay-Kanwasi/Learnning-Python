def factorial(num):
    if num == 0:
        return 1
    else: 
        return num * factorial(num-1)

while True:
    num = int(input("Enter the number : "))
    print(f"The factorial of {num} is {factorial(num)}.")