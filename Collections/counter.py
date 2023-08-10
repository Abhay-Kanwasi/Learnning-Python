from collections import Counter

a = 'aaaaaaabbbbbbb'
my_counter = Counter(a)
print(my_counter)   # returns a dictionary of key value
print(my_counter.items())   	# returns the list of key value
print(my_counter.most_common(1))    # returns a list tuple item inside it
print(my_counter.most_common(1)[0]) # returns a first item tuple
print(my_counter.most_common(1)[0][0])  # returns first item key 
print(list(my_counter.elements()))  # seperate all items and return a list



# math.prod(
import math
prime_factors = Counter({2:2, 3:3, 17:1})
# list(prime_factors.elements()) # Output : [2,2,3,3,3,17]
# print(math.prod(prime_factors.elements()))

list1 = prime_factors.elements()
print(math.prod(list1))