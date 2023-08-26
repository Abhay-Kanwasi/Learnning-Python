# Difference between two numbers 

number1 = int(input("Enter the number : "))
number2 = int(input("Enter the number : "))

difference = input('What type of difference you want with these two numbers\n1. Is they same or not.\n2. Who is greater between them\n3. Substraction between two numbers\nChoose your difference : ')

if difference == '1':
    if number1 != number2:
        print("Both numbers are different from each other.")
    else:
        print("Both numbers are same.")
elif difference == '2':
    if number1 > number2:
        print(f'{number1} is greater then {number2}')
    else:
        print(f'{number2} is greater than {number1}')
elif difference == '3':
    difference = number1 - number2
    print(f'{number1} - {number2} = {difference}')
else:
    print("Please choose between given choices..(e.g 1,2...)")