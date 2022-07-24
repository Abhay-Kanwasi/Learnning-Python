# Exponential power of a number.

# Using for loop

for i in range(10):
    power = 2**i
    print("2 raised to power",i,"is :",power)


# Using lambda functions

terms = 10

result = list(map(lambda x: 2**x,range(terms)))

for i in range(terms):
    print("2 raised to the power of ",i,"is",result[i])