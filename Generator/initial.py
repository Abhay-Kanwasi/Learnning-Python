# Generate allow us to generate a sequence of values over time.

print(list(range(10)))


def makelist(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = makelist(100)
print(my_list)