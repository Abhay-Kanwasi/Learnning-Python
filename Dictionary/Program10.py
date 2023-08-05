# Remove a key from a dictionary

dictionary = {'1':'10','2':'20','3':'30'}
key = input("Enter the key you want to remove : ")

print(f'Before deletion dictionary : {dictionary}')

del dictionary[key]
print(f'After deletion dictionary : {dictionary}')