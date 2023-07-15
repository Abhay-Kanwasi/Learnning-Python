# Write a program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
third_number = int(input("Enter the third number : "))

sum = first_number + second_number + third_number

if first_number == second_number == third_number:
    print(f"Because values are equal that's why it will printing the thrice of their sum which is {sum*3}.")
else:
    print(f'Sum of {first_number},{second_number},{third_number} is {sum}.')