# Write a program which accepts a sequence of comma-seperated numbers from user and generate a list and a tuple with those numbers.

sample_data = input("Enter a sequence of comma-seperated numbers : ")
list = sample_data.split(',') # split take a string and give output as a list
print(f'List : {list}')
print(f'Tuple : {tuple(list)}')
