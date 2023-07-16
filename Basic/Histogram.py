#  Program to create a historgram from a given list of integers.

def histogram(items):
    for  n in items:
        output = ''
        times = n
        while( times > 0 ):
            output += '*'
            times = times - 1
        print(output)

list = [2,3,6,5]
histogram(list)