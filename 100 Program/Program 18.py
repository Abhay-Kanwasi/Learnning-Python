# Simple Calculator 

def addtion(number1,number2):
    return f'Additon is : {number1 + number2}'

def subtraction(number1,number2):
    return f'Subtraction is : {number1-number2}'

def multiplication(number1,number2):
    return f'Multiplication is : {number1*number2}'

def division(number1, number2):
    try:
        division = number1/number2
        return f'Division is : {division}'
    except Exception as e:
        return f'Error : {e}'
    
print("CALCULATOR")
number1 = float(input("Enter the number : "))
number2 = float(input("Enter the number : "))

choice = int(input("Operations are : \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nChoose from one of them..\nYour choice : "))
if choice == 1:
    print(addtion(number1,number2))
elif choice == 2:
    print(subtraction(number1,number2))
elif choice == 3:
    print(multiplication(number1,number2))
elif choice == 4:
    print(division(number1, number2))
else:
    print("Please choose the right option..")
