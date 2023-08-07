""" 
# Define three functions fun(), disp(), msg(), store them in a list and call them one by one in a loop.

def func():
    print('This is func')

def disp():
    print("This is disp")

def msg():
    print('This is msg')

lst = [func, disp, msg]

for function in lst:
    function()


# Suppose there are two lists, one containing numbers from 1 to 6, and other containing numbers from 6 to 1. Write a program to obtain a list that contains elements obtained by adding corresponding elements of the two lists.

list1 = [1,2,3,4,5,6]
list2 = [6,5,4,3,2,1]

# Using function

# def add(list1,list2):
#     new_list = []
#     add = 0
#     for i in range(len(list1)):
#         add = list1[i] + list2[i]
#         new_list.append(add)
#     return new_list

# print(add(list1, list2))

# Using Map

obtained_list = list(map(lambda x,y : x + y, list1, list2))
print(obtained_list)


# Write a program to create a new list by obtaining square of all numbers in a list.

sample_list = [2,3,4,5]
square_contain_list = list(map(lambda x : x ** 2, sample_list))
print(square_contain_list)


# Can you make your own map function ?

# Yes I can let's make it acordingley :
def my_map(func, seq): # Takes two parameters function and sequence
    result = []        # Give a iterable sequence
    for element in seq:
        result.append(func(element))    # Apply function to every item
    return result   # Get new sequence as result

sequence = [2,3,4,5]
new_sequence = list(my_map(lambda x: x**2, sequence))

print(new_sequence)


"""
# Following data shows names, ages and marks of students in a class:
'''
Anil, 21, 80
Sohil, 20, 90
Sunil, 20, 91
Shobha, 18, 93
Anil, 19, 85

# Write a program  to sort this data on multiple keys in the order name, age and marks.

data = [
    ('Anil', 21, 80), 
    ('Sohil', 20, 90), 
    ('Sunil', 20, 91), 
    ('Sobha', 18, 93), 
    ('Anil', 19, 85)
]

sorted_data = list(sorted(data))
print(sorted_data)


'''
# Suppose a dictionary contain key-value pairs, where key is an alphabet and value is a number. Write a program that obtains that maximum and minimum form the dictionary.

container = {}
n = int(input("How many elements you want to add : "))
for item in range(n):
    key = input("Enter a alphabet : ")
    value = int(input("Enter the value : "))
    container[key] = value

print(max(container))
print(min(container))




