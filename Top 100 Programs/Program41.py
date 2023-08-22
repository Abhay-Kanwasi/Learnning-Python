# Perfect square 



# Method 1



# Method 2



# Method 3




# Method 4


# Perfect square between ranges




operation = int(input("What you want to do :\n1. Check for perfect square in a number\n2. Check for perfect square between a range.\nChoose operation : "))
if operation == 1:
    print("\nPerfect Square of a number\n")
    number = int(input("Enter the number : "))
    square_root = number ** 0.5
    choice = int(input("Which method to use :\n1. Method 1\n2. Method 2\n3. Method 3\n4. Method 4\nYour Choice : "))
    if choice == 1:
        print("Method 1\n")
        if int(square_root+0.5)**2 == number:
            print("It is a perfect square.")
        else:
            print("It is not a perfect square.")
    elif choice == 2:
        print("Method 2\n")
        if (number ** 0.5)**2 == number:
            print("It is a perfect square.")
        else:
            print("It is not a perfect square.")
    elif choice == 3:
        print("Method 3\n")
        if number**(0.5) == int(number**(0.5)):
            print("Perfect Square")
        else:
            print("Not perfect square")
    elif choice == 4:
        print("Method 4\n")
        import math

        math_square_root = math.sqrt(number)
        if math_square_root**2 == number:
            print("Perfect Square")
        else:
            print("Not perfect square")
    else:
        print("Please choice from method 1 to method 5 in integer format (e.g 1)")
if operation == 2:
    print("Perfect Square between two numbers\n")
    a = int(input("Start from : "))
    b = int(input("End to : "))

    for number in range(a, b+1):
        if number**0.5 == int(number**0.5):
            print(number, end=" ")
