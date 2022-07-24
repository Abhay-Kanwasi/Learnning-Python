# HCF of two number using division method 

# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter a number : "))
# if num2>num1:
#     remainder = num2%num1
#     if remainder//num2==0:
#         print("HCF of two numbers are :",remainder)
# else:
#     remainder = num1%num2
#     if remainder//num1==0:
#         print("HCF of two numbers are :",remainder)


# This code will not give output properly if remainder num1%num2 is 0.

# smaller = 0
# hcf = 0
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter a number : "))
# if num1>num2:
#     smaller = num2
# else: 
#     smaller = num1
# for i in range(1,smaller+1):
#     if(num1%i==0) and (num2%i==0):
#         hcf = i
# print("The HCF of two numbers is :",hcf)