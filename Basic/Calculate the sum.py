# Write a program to calculate the sum of all even numbers from 1 to 50.

sum = 0
a = 1
b = 51
for number in range(a,b):
    if number % 2 == 0:
        sum += number

print(f'Sum of all even numbers from {a} to {b} is {sum}.')