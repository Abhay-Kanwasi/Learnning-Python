# Calculator using lambda funtion 

class LambdaFunction:
    def Calculator():
        add = lambda a, b : a + b
        sub = lambda a,b : a - b
        mul = lambda a, b : a * b
        div = lambda a, b : a / b

        print('########## Calculator ###########')
        first_number = int(input("Enter the first number : "))
        second_number = int(input("Enter the second number : "))
        operation = int(input("Choose the operation :\n\tEnter 1 for addition\n\tEnter 2 for subtraction\n\tEnter 3 for multiplication\n\tEnter 4 for division\n\tEnter your choice : "))

        if operation == 1:
            print(f'Addition of two numbers : {add(first_number,second_number)}')
        elif operation == 2:
            print(f'Subtraction of two numbers : {sub(first_number,second_number)}')
        elif operation == 3:
            print(f'Multiplication of two numbers : {mul(first_number,second_number)}')
        elif operation == 4:
            try:
                print(f'Division of two numbers : {div(first_number,second_number)}')
            except ZeroDivisionError as e:
                print(f'Error occurs.. {e} error.')
        else:
            print("Please reconsider your choice..")
        

# LambdaFunction.Calculator()      # If you want to access the calculator


# Question 1 : Write a lamda function which takes a string as argument and strips away any whitespace and returns the uppercase version of string

Answer1 = lambda s : s.strip().upper().lower().title()
print(Answer1('ABHAYkAnWasi'))