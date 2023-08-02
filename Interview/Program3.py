# Write a python program to sort characters and numbers so that first alphabets and then number are printed.

# Input : A7B1R3
# Output : ABR137

string = input("Enter any string : ")

alphabets = []
numbers = []
for i in range(len(string)):
    if string[i].isdigit():
        numbers.append(string[i])
    if string[i].isalpha():
        alphabets.append(string[i])
    else:
        continue

final = sorted(alphabets) + sorted(numbers)
output = ''.join(final)
print(f'For string {string}\nThe output is : {output}.')