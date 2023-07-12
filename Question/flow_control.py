# Perfect square in Python

# Method 1

# import math

# num = int(input("Enter the number : "))
# root = math.sqrt(num)
# print(root)
# if int(root+0.5)**2==num:
#     print(num,"is a perfect square.")
# else:
#     print(num,"is not a perfect square.")


# Method 2

# import math 

# def PerfectSquare(x):
#     root = math.sqrt(x)
#     if int(root + 0.5)**2 == x:
#         print(x,"is a perfect square.")
#     else:
#         print(x,"is not a perfect square.")
#     return root

# num = int(input("Enter the nubmer : "))
# PerfectSquare(num)


# Method 3 : Without using sqrt()

def PerfectSquare(x):
    i = 1
    while(i**2 <= x):
        if ((x%i==0) and (x/i==i)):
            return True
        i += 1
    return False

num = int(input)

