# Create a fibonacci series with and without using recurssion

# 1, 1, 2, 3, 5, 8, 13


def fibonacci_series_with_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci_series_with_recursion(n - 2) + fibonacci_series_with_recursion(n - 1))


def fibonacci_series_without_recursion(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)


try: 
    n = int(input("How many terms you need of fibonacci series : "))
    choose = int(input("How you want to do it ?\n1. Using recursion \n2. Without using recursion \nYour choice : "))
    if choose == 1:
        for n in range(0, n):
           print(fibonacci_series_with_recursion(n))
    elif choose == 2:
        fibonacci_series_without_recursion(n)
except Exception as e:
    print(f'Error occurs during input\nError : {e}\nChoose either option 1 or option 2..')