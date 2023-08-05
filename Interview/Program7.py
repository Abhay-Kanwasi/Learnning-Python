# Count the occurence of a number in a string and also print character and it's count.

# string = input("Enter the string : ")
# counts = []
# numbers = [] 
# count = 0
# for i in string:
#     if i.isdigit() == True:
#         numbers.append(i)
#         count = string.count(i)
#         # count = sum(1 for char in string if char == i)
#         counts.append(count)
# print(numbers, counts)


string = input("Enter the string: ")
counts = []
numbers = []

for i in string:
    if i.isdigit():
        if i not in numbers:
            numbers.append(i)
            count = string.count(i)
            counts.append(count)

number_count = [i for i in numbers]
counter_count = [i for i in counts]
answer = dict(zip(number_count, counter_count))
print('Output {number : counts} : ',answer)

