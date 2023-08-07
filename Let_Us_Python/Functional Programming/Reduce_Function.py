from functools import reduce

lst1 = [2,3,45]
lst2 = list(reduce(lambda n: n*n, lst1))