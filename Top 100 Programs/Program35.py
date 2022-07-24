# Swapping two numbers with the help of two variables
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))

c = a # Now c contains the value of a. 
a = b # Now a contains the value of b and loose it's orignal value
b = c # Now b contains the value of c ('c' contains the value of a.)\

# Now the numbers succesfully swapped.

print("The value of a is :",a)
print("The value of b is :",b)
