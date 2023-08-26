# Find factors of a number in python 

number = int(input("Enter the number : "))

print(f'The factors of number {number} are : \n')
print('\nUsing for loop')
for i in range(1,number+1):
    if number % i == 0:
        print(i, end=' ')

print('\n\nUsing while loop')
i = 1
while i<=number:
    if number % i == 0:
        print(i, end=" ")
    i += 1
