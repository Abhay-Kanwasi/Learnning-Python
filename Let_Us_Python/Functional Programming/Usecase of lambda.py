d = {'Oil':230, 'Clip':150, 'Stud':175, 'Nut':35}
d1 = sorted(d.items(), key= lambda key_or_value : key_or_value[0]) #0 is for key and 1 is for value.

# In this code d1 is a variable that stores the value of sorted items of d dictionary according to key which is in our case is value kv[1] if we put kv[0] then the condition of sorting will change and it will sorted accordingly to dictionaryt keys
print(d1)

