# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

list2 = []
list = [1,2,3,4,5,6,7]
for i in range(len(list)):
    if i == 2:
        list2.append(list[i])
        list.remove(list[i])
    

print(list2)
    
# Doesn't working at all
