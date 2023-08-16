# Create a list of numbers and use a loop to find the sum of all numbers in the list.

numbers = [2,3,4,5]
sum = 0
for number in numbers:
    sum += number
print(sum)

# Write a Python function to find the factorial of a given positive integer.


# Implement a program that swaps the values of two variables without using a temporary variable.

a = 2# int(input("Enter the number a : "))
b = 3# int(input("Enter the number b : "))

a = a + b
b = a - b
a = a - b
print(f'a : {a}\nb : {b}')

# Create a function that takes a list of integers and returns a new list with only the even numbers.

list_of_numbers = [2,3,4,5,6]
new_list = []
for number in list_of_numbers:
    if number % 2 == 0:
        new_list.append(number)
print(f'Old list : {list_of_numbers}\nNew list : {new_list}')



# Write a program to generate the Fibonacci sequence up to the nth term.


# Implement a function that checks if a given string is a palindrome (reads the same forwards and backwards).

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
string = 'aba' # input("Enter the string : ")
print(is_palindrome(string))