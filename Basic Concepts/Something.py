# Pack first 10 multiples of 10 into a tuple

tuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Unpack the tuple into 10 variables, each holding 1 value.
# a,b,c,d,e,f,g,h,i,j = tuple1
# print(tuple1)
# print(a,b,c,d,e,f,g,h,i,j)

# list = ['Shubham', 'Nisha', 'Sudha', ('Suresh',),('Rajesh',),'Radha']
# boys = 0
# girls = 0
# for i in list:
#     if isinstance(i, tuple):
#         boys+=1
#     else:
#         girls+=1
# print(boys)
# print(girls)

# from datetime import date

# date1 = date(2012, 12, 12)
# date2 = date(2023, 11, 11)

# difference = date2 - date1
# print(difference.days)


# tuples = [('item1','22.2'),('item2', '2.4'),('item3', '3.2')]
# print(sorted(tuples, key=lambda a: float(a[1]), reverse=True))

# user = (
#     ('Share name','TATA'),
#     ('Date of purchase','20Dec2019'),
#     ('Cost price','2.0LPA'),
#     ('Number of shares','10'),
#     ('Selling price','2.7LPA'),
#     )

set1 = {12,15,13,23}
t = {'A', 'B', 'C'}

set1.update(t)

set1.add('H')
print(set1)

set1.remove(15)
print(set1)

set1.discard(101) # even element doesn't exist it's not giving me error.

set1.clear()
print(set1)

set1 = {'Abhay', 'Akash','Bohimiya','Brad','Ammu'}

set1 = list(set1)

aset = set()
bset = set()

for name in set1:
    if name[0] == 'A':
        aset.add(name)
    elif name[0] == 'B':
        bset.add(name)
    else:
        continue

print(aset)
print(bset)

##################################################

import random

numbers = set()
count = 0
for num in range(10):
    numbers.add(random.randint(15,45))
print(numbers)
numbers = list(numbers)
for num in numbers:
    if num < 30:
        count += 1
    if num > 35:
        numbers.remove(num)
print(numbers)
print(count)
