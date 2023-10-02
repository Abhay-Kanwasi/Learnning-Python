# How to get all the keys of dictionary

dictionary1 = {'a':'apple', 'b':'ball', 'c':'cat', 'd':'dog'}
print(dictionary1.keys())

# How to get all the values of dictionary

dictionary2 = {'a':'apple', 'b':'ball', 'c':'cat', 'd':'dog'}
print(dictionary2.values())

# How to get all the key value of dictionary

dictionary3 = {'a':'apple', 'b':'ball', 'c':'cat', 'd':'dog'}
print(dictionary3.items())

# Remove item using dictionary pop method

dictionary4 = {'a':'apple', 'b':'ball', 'c':'cat', 'd':'dog'}
dictionary4.pop('a')
print(dictionary4)

# Remove item using dictionary pop item method

dictionary5 = {'a':'apple', 'b':'ball', 'c':'cat', 'd':'dog'}
dictionary5.popitem()
print(dictionary5)

# Remove item using dictionary del method

dictionary6 = {'a':'apple', 'b':'ball', 'c':'cat', 'd':'dog'}
del(dictionary6['d'])
print(dictionary6)

# Creating a new dictionary from iterable

key_lst = ['at','an', 'am', 'as']
value_lst = [11,12,13,14,15]

new_dictionary = {}

for new in range(len(key_lst)):
    new_dictionary[key_lst[new]] = value_lst[new]

print(new_dictionary)

dict_sub = {key:value for(key,value) in zip(key_lst, value_lst)}
print(dict_sub)

# Single condition with dictionary comprehension

dictionary7 = {'ram':23, 'shaam':89, 'ghansam':4, 'radha':6}

single = {(key,value) for (key,value) in dictionary7.items() if value%2==0}
print(single)

# Multiple condition with dictionary comprehension

dictionary8 = {'ram':23, 'shaam':89, 'ghansam':40, 'radha':6}
multiple = {(key,value) for(key,value) in dictionary8.items() if value > 20 or value%2==0}
print(multiple)

# How to change a name in dictionary 

dictionary8 = {'ram':23, 'shaam':89, 'ghansam':40, 'radha':6}
dictionary8['ravan'] = dictionary8.pop('ram')
print(dictionary8)

# How to change value of any key in nested dictionary

animal_dict = {
    "animal" : {
        "name" : "Dog",
        "age" : 5
    },
    "animal1" : {
        "name" : "Cat",
        "age" : 2
    },
    "animal2" : {
        "name" : "Rabbit",
        "age" : 1
    }
}

animal_dict['animal']['name'] = "Ekta"
print(animal_dict['animal']['name'])

# How to delete a key from the dictionary

fruitsDict = {
    'Apple' : 110,
    'Orange' : 230,
    'Banana' : 400,
    'Pomegranate' : 250
}

del(fruitsDict['Apple'])
print(fruitsDict)

# How to get the minimum and maximum keys corrospoding to min and max value in dictionary

fruitsDict1 = {
    'Apple' : 110,
    'Orange' : 230,
    'Banana' : 400,
    'Pomegranate' : 250
}

print(f'Minimum key is {min(fruitsDict1.keys())} and minimum value is {min(fruitsDict.values())}')
print(f'Maximum key is {max(fruitsDict1.keys())} and maximum value is {max(fruitsDict.values())}')


# How to concatenate multiple dictionary in one

dictionary9 = {'a':'apple', 'b': 'ball'}
dictionary10 = {'c':'cat', 'd': 'dog'}
dictionary11 = {'e':'egg', 'f': 'fish'}

concatenated = {}

for dictionary in (dictionary9, dictionary10, dictionary11):
    concatenated.update(dictionary)

print(concatenated)

# How to get the sum of all the elements of dictionary

fruitsDict2 = {
    'Apple' : 110,
    'Orange' : 230,
    'Banana' : 400,
    'Pomegranate' : 250
}

print(sum(fruitsDict.values()))


# How to multiply all teh elements of dictionary

fruitsDict3 = {
    'Apple' : 110,
    'Orange' : 230,
    'Banana' : 400,
    'Pomegranate' : 250
}

result = 1
for value in fruitsDict3.values():
    result = result * value
print(result)


# How to sort a dictionary by key 

fruitsDict4 = {
    'Apple' : 110,
    'Orange' : 230,
    'Banana' : 400,
    'Pomegranate' : 250
}

print("Sorted Dictionary : ")
try :
    for keyvalue in sorted(fruitsDict4.items()):
        print('%s %s' % (keyvalue, fruitsDict4[keyvalue]))
except KeyError:
    print(KeyError)

# How to print dictionary as table

dict_tab = {'Students' : ['Rack', 'Jack', 'Jhon'], 'Fruits' : ['Apple', 'Banana', 'Orange'], 'Subjects' : ['Phy', 'Math', 'English']}

for row in zip(*([key] + (value) for key, value in sorted(dict_tab.items()))):
    print(*row)