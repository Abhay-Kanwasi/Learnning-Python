# How to find smallest number in list with the help of min function.

list1 = []
length = int(input("How many numbers you want to store in a list :"))
for i in range(length):
    a = int(input("Enter a number :"))
    list1.append(a)
print("The smallest number in the list :",min(list1))