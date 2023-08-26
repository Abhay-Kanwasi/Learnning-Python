# Fibonacci Series

series = int(input("How much numbers you want in your fibonacci series : "))

a, b = 0, 1

count = 0

if series <= 0:
    print("Please enter the positive number.")
elif series == 1:
    print('Fibonacci series : {0}'.format(a))
else:
    operation = input("Which operation you want to perform\n1. for loop\n2. while loop\nYour option : ")
    if operation == '1':
        print("Fibonacci series :")
        for i in range(1, series+1):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

    elif operation == '2':
        print('Fibonacci series : ')
        while count < series:
            print(a, end=" ")
            c = a + b
            a = b
            b = c
            count += 1
    else:
        print("Please choose either 1 or 2")


