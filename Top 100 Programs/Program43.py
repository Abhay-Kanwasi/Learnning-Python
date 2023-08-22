# Simple calculator 

while True:
    number1 = int(input("Enter the number : "))
    operation = input("Operation : ")
    number2 = int(input("Enter the number : "))
    print(f'Your operation : {number1} {operation} {number2}')
    if operation == '+':
        print(f'result : {number1 + number2}')
    elif operation == '-':
        print(f'result : {number1 - number2}')
    elif operation == '*':
        print(f'result : {number1 * number2}')
    elif operation == '/':
        try:
            print(f'result : {number1 / number2}')
        except ZeroDivisionError as e:
            print(f'Error : {e}')
    elif operation == '%':
        print(f'result : {number1 % number2}')
    elif operation == '//':
        print(f'result : {number1 // number2}')
    elif operation == '==':
        print(f'result : {number1 == number2}')
    elif operation == '!=':
        print(f'result : {number1 != number2}')
    else:
        print("Don't find this operation in your calculator.")
    
    

    again = input("Do you want to perform another calculation? (Yes/No): ").lower()
    if again == 'no':
        break
    elif again != 'yes':
        print("Please choose the right option")