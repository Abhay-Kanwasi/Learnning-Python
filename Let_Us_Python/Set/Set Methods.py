# Wants to add element in set 

numbers = {12,15,13,16,17,1}
alphabets = {'a', 'b', 'c'}

numbers.update(alphabets)

print(numbers)

# add a single value 

alphabets.add('d')
print(alphabets)

# remove elements 

alphabets.remove('a') # if value not present in set it will raise error
print(alphabets)

alphabets.discard('f') # It doesn't raise any error if the value is not in set
print(alphabets)


# clear all the values
alphabets.clear()
print(alphabets)


# check relationship between two sets

set1 = {1,2,3,4,5,6,7}
set2 = {1,2,3}

print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))