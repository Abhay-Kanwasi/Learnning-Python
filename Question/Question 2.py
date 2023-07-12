# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import random
import time
while True:
    char_list = ['a','e','i','o','u']
    random.shuffle(char_list)
    print(''.join(char_list))
    time.sleep(2)

# Problem 1 : How can we use loop in this program 
# Problem 2 : If we use this method than how can we stop it after it give use all the possible strings without any repetation of same string(although i also don't know is it give us a string which is comes one time already.)
