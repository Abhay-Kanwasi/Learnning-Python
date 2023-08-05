# Sum of all the items in the dictionary

dictionary = {'1':'10','2':'20','3':'30'}

sum = 0
for i in dictionary.values():
    sum += int(i)

print(sum)