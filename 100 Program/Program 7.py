# Swap two numbers

numberA = int(input('Enter the first number : '))
numberB = int(input('Enter the second number : '))
print(f'NumberA and NumberB before swapping is {numberA} and {numberB}')

logic = int(input("Choose the logic :\n1. Using temprory variable\n2. Using pack unpack\n3. Using operators\nYour choice : "))

if logic == 1:
    temprory_variable = numberA
    numberA = numberB
    numberB = temprory_variable
    print(f'NumberA and NumberB after swapping is {numberA} and {numberB}')
elif logic == 2:
    numberA,numberB = numberB,numberA
    print(f'NumberA and NumberB after swapping is {numberA} and {numberB}')
elif logic == 3:
    numberA = numberA + numberB
    numberB = numberA - numberB
    numberA = numberA - numberB
    print(f'NumberA and NumberB after swapping is {numberA} and {numberB}')
else:
    print("Please choose between 3 options.")




