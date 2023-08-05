# Check whether a given key already exist in dictionary

dictionary = {'1': '10',
              '2': '20',
              '3': '30',
              '4': '40'
              }
key = input("Enter the key  :")
if key in dictionary.keys():
    print(True)
else:
    print(False)