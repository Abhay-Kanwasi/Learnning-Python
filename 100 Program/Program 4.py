# Divide two number

number1 = int(input("Enter the number : "))
number2 = int(input("Enter the number : "))

try:
    divison = number1/number2
    print(f'Division of {number1} and {number2} is {divison}.')
except ZeroDivisionError as e:
    print(f'Error : {e} error.')
