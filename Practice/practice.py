# Check if a string is palindrome or not

string = "abhbai"

# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# palindrome_string = ""
# for i in string:
#     palindrome_string = i + palindrome_string

# if string == palindrome_string:
#     print("This is an palindrome")
# else:
#     print("This is not an palindrome")


#################################################################

# Write a python program to find the factorial of a number.

number = 7
factorial = 1
for i in range(number):
    i += 1
    factorial = factorial * i
print(factorial)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(f"Factorial : {factorial(7)}")

#####################################################################

# Write a python program to find the largest element in a list.

list = [2,5,4,8,7,22,4,8,9]

sum = 0
for i in list:
    if sum < i:
        sum = i
    continue

print(sum)

print(max(list))

######################################################################

# Write a Python program to reverse a string.

string = "abhay"
print(string[::-1])

reverse = ""
for i in string:
    reverse = i + reverse
print(reverse)


#########################################################################

# Write a Python program to count the frequency of each element in a list.

numbers = [2,3,2,4,3,4,5,5,6,7,1]
unique_elements = set(list)


frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
