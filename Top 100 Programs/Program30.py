# Find smallest number in a list using append method.

# list1 = [11,12,32,43,31,23]
# list2 = []
# for i in list1:
#     list2.append(i)
# print("The smallest number in the list is :",min(list2))


list2 = []

length = int(input("How many numbers you want to store :"))
for i in range(length):
    a = int(input("Enter the number :"))
    list2.append(a)
print("The smallest number in the list is:",min(list2))    
