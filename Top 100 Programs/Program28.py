# How to find largest number in a list append method.

# Can be done it like this

list1 = [11,12,23,47,1,44]
list1.sort()
print(list1[-1])

# Now using append method

list2 = []
list1 = [11,13,22,43,34,55,1]
for i in list1:
    list2.append(i)
print("The largest number in list is :",max(list2))




