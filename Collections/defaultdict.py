# Similar to usual dictionary container only difference that it will have a default value if key is been not set yet.

from collections import defaultdict

dic = defaultdict(int) # default type int

dic['a'] = 1
dic['c'] = 11
dic['b'] = 12
dic['d'] = 31

print(dic['e']) # If item doesn't exist it will print default int value 

