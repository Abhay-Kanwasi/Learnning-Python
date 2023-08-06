# All map() related questions



# Finding square root of all numbers in the list and returning a list of these roots.

list1 = [1,2,3,4]

"""
First Step : new_list = map(function, iterable) # Function : lambda x : x**2, Iterable : list1
Second Step : new_list = map(lambda x : x**2, list1)
Third Step : new_list = list(map(lambda x: x**2, list1)) # Convert it into list because it will give a iterable object to us
"""
new_list = list(map(lambda x: x**2, list1))
print(new_list) # Because it will give us iterable result