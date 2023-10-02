# # Pack first 10 multiples of 10 into a tuple

# tuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# # Unpack the tuple into 10 variables, each holding 1 value.
# # a,b,c,d,e,f,g,h,i,j = tuple1
# # print(tuple1)
# # print(a,b,c,d,e,f,g,h,i,j)

# # list = ['Shubham', 'Nisha', 'Sudha', ('Suresh',),('Rajesh',),'Radha']
# # boys = 0
# # girls = 0
# # for i in list:
# #     if isinstance(i, tuple):
# #         boys+=1
# #     else:
# #         girls+=1
# # print(boys)
# # print(girls)

# # from datetime import date

# # date1 = date(2012, 12, 12)
# # date2 = date(2023, 11, 11)

# # difference = date2 - date1
# # print(difference.days)


# # tuples = [('item1','22.2'),('item2', '2.4'),('item3', '3.2')]
# # print(sorted(tuples, key=lambda a: float(a[1]), reverse=True))

# # user = (
# #     ('Share name','TATA'),
# #     ('Date of purchase','20Dec2019'),
# #     ('Cost price','2.0LPA'),
# #     ('Number of shares','10'),
# #     ('Selling price','2.7LPA'),
# #     )

# # set1 = {12,15,13,23}
# # t = {'A', 'B', 'C'}

# # set1.update(t)

# # set1.add('H')
# # print(set1)

# # set1.remove(15)
# # print(set1)

# # set1.discard(101) # even element doesn't exist it's not giving me error.

# # set1.clear()
# # print(set1)

# # set1 = {'Abhay', 'Akash','Bohimiya','Brad','Ammu'}

# # set1 = list(set1)

# # aset = set()
# # bset = set()

# # for name in set1:
# #     if name[0] == 'A':
# #         aset.add(name)
# #     elif name[0] == 'B':
# #         bset.add(name)
# #     else:
# #         continue

# # print(aset)
# # print(bset)

# ##################################################

# # import random

# # numbers = set()
# # count = 0
# # for num in range(10):
# #     numbers.add(random.randint(15,45))
# # print(numbers)
# # numbers = list(numbers)
# # for num in numbers:
# #     if num < 30:
# #         count += 1
# #     if num > 35:
# #         numbers.remove(num)
# # print(numbers)
# # print(count)

# #####################################################

# # string1 = "sldf"
# # tuple1 = (2,1,2,3)
# # list1 = [1,2,3,1,3,1,1]

# # string2 = set(string1)
# # string3 = ''.join(string2)

# # print(f'Before : {string1} | After : {string3}')
# # print(f'Before : {tuple1} | After : {set(tuple1)}')
# # print(f'Before : {list1} | After : {set(list1)}')


# # tuple1 = set(tuple1)
# # tuple1.clear()
# # print(tuple1)

# # del(tuple1)
# # # print(tuple1)

# # s1 = set()
# # print(type(s1))

# # s3 = {2,}
# # print(type(s3))

# # #######################################################

# # b = {'A101':'Amol', 'A102':'Anil','B103':'Ravi'}
# # lst = {12,13,14,15,16}
# # e = dict.fromkeys(lst, 2)
# # print(e)

# # courses = {
# #     'DAA':'CS',
# #     'AOA':'ME',
# #     'SVY':'CE'
# #     }

# # print("Key | Values")
# # for key,value in courses.items():
# #     print(key,"|",value)

# # print("\nKeys")
# # for key in courses.keys():
# #     print(key)

# # print("\nValues")
# # for values in courses.values():
# #     print(values)

# # # Dictionary operations

# # courses = {
# #     'CS101' : 'CPP',
# #     'CS102' : 'DS',
# #     'CS201' : 'OOP',
# #     'CS226' : 'DAA',
# #     'CS601' : 'Crypt',
# #     'CS442' : 'Web'
# # }
# # print(courses)

# # # add new course
# # courses['CS302'] = 'AI'
# # print(courses)

# # # modify existing course
# # courses['CS101'] = 'ML'
# # print(courses)

# # # delete course item
# # del(courses['CS201'])
# # print(courses)

# # # delete entire course
# # # del(courses)
# # print(courses)

# # d1 = {'CS677': 'Python'}
# # courses.update(d1)

# # print(courses)

# # ##################################

# # students = {'Abhay' : '21', 'Abishek' : '22', 'Sachin' : '19'}
# # stud = students
# # students = {}
# # print(stud)

# ###################################

# # cricketers = ['Sunil', 'Sachin', 'Aswin', 'Jadeja','Sunil']
# # d = dict.fromkeys(cricketers, 50)
# # print(d)

# # ###################################

# # dictionary = {'Abhay':1, 'Abhishek':2, 'Aman':3, 'Anshul':4}

# # print("\nSorted by key\n")
# # print(sorted(dictionary.items()))
# # print(sorted(dictionary.items(), reverse=True))


# # from operator import itemgetter
# # # dictionary = sorted(dictionary.items(), key=itemgetter(1))
# # # print(dictionary)

# # dictionary = sorted(dictionary.items(), key=itemgetter(1), reverse=True)
# # print(dictionary)

# dictionary1 = {'Mango':30, 'Guava':34}
# dictionary2 = {'Apple':70, 'Pineapple':50}
# dictionary3 = {'Kiwi':90, 'Banana':35}

# dictionary4 = {}

# # for dictionary in (dictionary1, dictionary2, dictionary3):
# #     dictionary4.update(dictionary)

# dictionary4 = {*dictionary1, *dictionary2, *dictionary3}

# print(dictionary4)

# ########################################################

# dictionary5 = {"Abhay": 1}
# # if bool(dictionary5):
# #     print("Dictionary is not empty.")
# # else:
# #     print("Dictionary is empty.")

# if dictionary5 == {}:
#     print('Dictionary is empty.')
# else:
#     print("Dictionary is not empty.")

# ########################################################

# boys = {'ram':20, 'shaam':30, 'ruman':40}
# girls = {'sita':34, 'geeta':22, 'rita': 25}

# students = {}

# # for student in (boys, girls):
# #     students.update(student)
# # print(students)

# students = {**boys, **girls}
# print(students)

# ###########################################################
# d = {
#     'anuj':{'salary': 10000, 'age' : 20, 'height' : 6},
#     'aditya':{'salary': 6000, 'age' : 26, 'height' : 5.6},
#     'rahul':{'salary': 7000, 'age' : 26, 'height' : 5.9},
# }

# list = []
# for salary in d.values():
#     list.append(salary['salary'])

# print(f'Maximum Salary : {max(list)}')
# print(f'Minimum Salary : {min(list)}')

# #############################################################
# students = {554 : 'Ajay', 350 : 'Ramesh', 395 : 'Rakesh'}

# rollno = int(input("Enter the roll no. : "))
# name = students.get(rollno, 'Student')
# print(f'Congrats ! {name}')

# rollno = int(input("Enter the roll no. : "))
# name = students.get(rollno, 'Student')
# print(f'Congrats ! {name}') 

##############################################################

# import random
# a = [random.randint(10,200) for num in range(20) if num%2==0]
# print(a)


# numbers = {(num, num**2, num**3) for num in range(1,10)}
# print(numbers)


# List Comprehension
# convert a list of strings to a list of integers
# integers = [int(string) for string in ['10','20','30','40','50']]
# print(integers)

# Set comprehension
# print("In 'Technical'")
# a = {'vowels' if alphabets in 'aeiou' else 'consonent'  for alphabets in 'Technical'}
# print(a)

# Dictionary comprehension
# dict = {'a' : 'apple', 'b' : 'ball', 'c' : 'cat', 'd' : 'dog', 'e' : 'egg'}
# dict_var = {key: value for (key, value) in dict.items()}
# print(dict_var)

# numbers = [num for num in range(2,50) if num%2==0 and num%4==0]
# print(numbers)

# mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# flattern = [number for list1 in mat for number in list1]
# print(flattern)

# import random
# count = 0
# numbers = {random.randint(15,45) for number in range(10) }
# less_then_thirty = {number for number in numbers if number < 30}
# lenght_of_less_than_thirty = len(less_then_thirty)
# string = {num for num in numbers if num<30}
# numbers = numbers - string
# print(numbers) 