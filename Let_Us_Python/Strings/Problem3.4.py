# Given the following string:
'Bring It On'
'   Flanked by spaces on either side    '
'C:\\Users\\Kanetkar\\Documents'

# Produce the following output using appropriate string functions.

'''
'BRING IT ON'
'bring it on'
'Bring it on'
'bRING it oN'
'6'
'9'
'Bring Him On'
'Flanked by spaces on either side'
'   Flanked by spaces on either side'
['C', 'User','Kanetkar','Documents']
['C','\\','Users\\Kanetkar\\Documents']
'''

string1 = 'Bring It On'
string2 = '   Flanked by spaces on either side    '
string3 = 'C:\\Users\\Kanetkar\\Documents'

print(string1.upper())
print(string1.lower())
print(string1.capitalize())
print(string1.swapcase())
print(string1.find('I'))
print(string1.find('On'))
print(string1.replace('It','Him'))
print(string2.lstrip())
print(string2.rstrip())
print(string3.split('\\'))
print(string3.partition('\\'))