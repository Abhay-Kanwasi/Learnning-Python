# Question 1
def sum_of_all(list):
    sum = 0
    for i in sum_of_all:
        sum += i
    print(f"The sum of all the numbers in the list is {sum}.")

# Question 2
def multiply_of_all(list):
    multiply = 1
    for i in multiply_of_all:
        multiply *= i
    print(f"The multiply of all the items in the given list is {multiply}.")

# Question 3
def largest_number(list,choice):
    if choice == 2:
        largest = list[0]
        for i in list:
            if i>largest:
                largest=i
        print(f"Largest number in the list is {largest}.")
    if choice == 1:
        print(f"Largest number in the list is {max(list)}.")
    else:
        print("Try Again!")

# Question 4
def smallest_number(list,choice):
    if choice == 2:
        smallest = list[0]
        for i in list:
            if i<smallest:
                smallest = i
        print(f"Smallest number in the list is {smallest}.")
    if choice == 1:
        print(f"Smallest number in the list is {min(smallest_number)}.")
    else:
        print("Try Again!")

# Question 5
def first_last_character_same(list):
    list2 = []
    for i in range(len(list)):
        # We are using it as 2D array
        if list[i][0] == list[i][-1]:
            list2.append(i)
    print("Result : ",list2)

# first_last_character_same(['cbc','xyz','aba','1221'])

# Question 6

# Using sorted method
# def last(n): return n[-1]
# sample_list = [(2,5),(1,2),(4,4),(2,3),(2,1)]
# print(sorted(sample_list,key=last))

# Using bubble sort method
def Sorted_in_increasing_order(list):
    length = len(list)
    for i in range(0,length):
        for j in range(0,length-i-1):
            if list[j][-1] > list[j+1][-1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list        

sample_list = [(2,5),(1,2),(4,4),(2,3),(2,1)]
# print(Sorted_in_increasing_order(sample_list))

# Question 7

def remove_duplicates(list):
    list = set(list)
    return list

# list = [2,1,3,1,1]
# print(remove_duplicates(list))

# Question 8

def isempty(list):
    if len(list) == 0:
        print("List is empty.")
    else:
        print(f"List have {len(list)} items.")

# list = []
# isempty(list)

# Question 9

def clone_of_list(list):
    new_list = list.copy()
    print("Copied :",new_list)

# list = [1,2,3,4,5]
# clone_of_list(list)

# Question 10

def longer_words(list,n):
    n = int(input("Enter the minimum length of the word : "))
    list = ["Abhay","Kanwasi","Abhi","Subtle","of","fffffff"]
    list2 = []
    for i in list:
        if len(i) > n:
            list2.append(i)
    print(f"List of words that are longer than {n}: {list2}")


# Question 11

def common(list1,list2):
    for i in list1: 
        for j in list2:
            if i == j:
                return True
            else:
                continue
    return False

# list1 = [2,3,4,5]
# list2 = [1,0,2,7]
# print(common(list1,list2))

# Question 12

Sample_list = ['Red','Green','White','Black','Pink','Yellow']
Sample_list.pop(0)
Sample_list.pop(4)
Sample_list.pop(-1)
# print(Sample_list)

# Question 13

array = [[['*' for i in range(6)] for j in range(4)]for k in range(3)]
# print(array)


# Question 14

Specified_list = [2,3,5,6,7,9,12,11]
Specified_list = [x for x in Specified_list if x%2!=0]
# print(Specified_list)

# Question 15

def shuffle(list):
    from random import shuffle
    shuffle(list)
    return list

list5 = [2,3,4,6,8,10]
# print(shuffle(list5))

# Question 16

list1 = []
for i in range(1,31):
    list1.append(i**2)
# print(list1[:5])
# print(list1[-5:])

# Question 17

list2 = []
for i in range(1,31):
    list2.append(i**2)
# print(list2[5:])


# Question 18

import itertools
# print(list(itertools.permutations([1,2,3])))

# Question 19

listA = [2,3,4,5,6]
listB = [2,5,9,10,11]

diff_listA_and_listB = list(set(listA)-set(listB))
diff_listB_and_listA = list(set(listB)-set(listA))
Calculation = list(diff_listB_and_listA + diff_listA_and_listB)
# print(f"Diffrence between the two lists : ",Calculation)

# Question 20

listC = [2,4,6,8,1]
for i in range(len(listC)):
    pass
    # print(f"Index : {i} Value : {listC[i]}")

# Question 21
string = ""
list_of_characters = ['A','b','h','a','y']
for i in list_of_characters:
    string += i
# print("String is",string)

# Question 22

list_22 = [10,30,4,-6]
# print(list_22)
# value = int(input("Enter the value : "))
# print(f"Index of the value is : {list_22.index(value)}")

# Question 23

list_23 = [[10,20,30],[40,50,60],[70,80,90]]
flatlist = []
for sublist in list_23:
    for item in sublist:
        flatlist.append(item)
# print(flatlist)


# Question 24

orignal_list = [12,24,36,48]
second_list = []
for item in orignal_list:
    second_list.append(item)
# print(orignal_list)

# Question 25

import random
list25 = [2,3,4,5]
# print(random.choice(list25))

# Question 26

def circular_identical(list_1, list_2):
    list_3 = list_1 * 2
    for x in range(0, len(list_1)):
        z = 0
        for y in range(x, x + len(list_1)):
            if list_2[z]== list_3[y]:
                z+= 1
            else:
                break
        if z == len(list_1):
            return True
    return False

list_1 = [1, 2, 1, 1, 3]
list_2 = [3, 1, 2, 1, 1]
list_3 = [2, 1, 1, 2, 1]

# print("List one and two are being checked")
# if(circular_identical(list_1, list_2)):
#     print("Yes")
# else:
#     print("No")

# print("List two and three are being checked")
# if(circular_identical(list_2, list_3)):
#     print("Yes")
# else:
#     print("No")


# Question 27 

list27 = [1,2,3,4]
list27.remove(min(list27))
# print("Second last element in the list is :",min(list27))

# Question 28

list28 = [1,2,3,4]
list28.remove(max(list28))
# print("Second largest number in the list is :",max(list28))


# Question 29

list29 = [1,2,2,4,1]
list29_A = set(list29)
# print("Unique items in the list are :",list29_A)

# Question 30

list30 = [1,1,2,2,2,3,3,5,5,5,5]
frequency = {}

for i in list30:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

# print(frequency)

# Question 31

list31 = [10,20,30,40,40,40,70,80,99]
range1 = int(input("Starting range : "))
range2 = int(input("Ending range : "))
count = 0
for i in list31:
    if i>=range1 and i<=range2:
        count += 1
# print("Number of elements :",count)

# Question 32





