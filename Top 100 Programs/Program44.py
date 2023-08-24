# Fibonacci Series 

num = int(input("Enter number of terms : "))
a, b = 0, 1
if num <= 0:
    print("Please enter the positive number")
elif num == 1:
    print("Fibonacci series :")
    print(a)
else:
    print("Fibonacci series :")
    i =0 
    while i < num:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
        i = i + 1
