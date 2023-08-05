# Concatenate 3 dictionaries to make a new one

dictionary1 = {1:10,2:20}
dictionary2 = {3:10,4:20}
dictionary3 = {5:10,6:20}

new = {}

new.update(dictionary1)
new.update(dictionary2)
new.update(dictionary3)

print(new)