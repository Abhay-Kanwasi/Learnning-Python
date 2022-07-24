#Factorial of a number

#Basic =? Factorial of 4 = 4*3*2*1

# Factorail using for loop

num = int(input("Enter a number : "))
fact = 1
for i in range(num,0,-1):
    fact = fact * i
    print(i,"*",end="")
print("\nTotal factorial is : ",fact)



# Factorial using Recursion

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)
n = int(input("Enter a number :"))
if n<0:
    print("Negative numbers don't give factorial.")
if n==0:
    print("The factorial of 0 is :",1)
if n>0:
    print("The factorial of",n,"is :",fact(n))

