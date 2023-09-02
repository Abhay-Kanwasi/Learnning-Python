tuples = (2,3,2,4,2,3)

repeated_number = []

for number in tuples:
    if tuples.count(number) > 1 and number not in repeated_number:
        repeated_number.append(number)

# for item in repeated_number:
#     print(item, end=" ")

string = ''
for item in repeated_number:
    string += str(item) + ' '
print(string)
