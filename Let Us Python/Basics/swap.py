# Write a program that swaps the values of variables a and b. You are not allowed to use a third variable . You are not allowed to perform arithmetic  on and b.

# First let's do it with third variable

print("Using third variable \n")
a = 3
b = 4
temp = 0
print(f'The value of a is {a}, and the value of b is {b}.')

temp = a
a = b
b = temp

print(f'The value of a is {a}, and the value of b is {b}.')


print("\n\n With using arithmetic operation ")

a,b = b,a
print(f'The value of a is {a}, and the value of b is {b}.')


