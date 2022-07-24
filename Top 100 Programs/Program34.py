# In a list find numbers divisible by a number.

list1 = [10,12,24,96,108,56]
list2 = []
n = int(input("Enter the number :"))
for i in list1:
    if i%n==0:
        list2.append(i)
print("The number divisble by",n,"are :",list2)


list3 = [12,23,24,36,98,108,120]
n = int(input("Enter a number :"))
result = list(filter(lambda x:(x%n==0),list3)) 
print("The numbers divisible by",n,"are :",result)   

