# It's create the items one by one
# print(range(100))
#
# # It's create a giant list of 100 items in our computers memory
# print(list(range(100)))


# Creating a decorator to test who fast my code runs

from time import time


# Creating a decorator
def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"It took {end_time - start_time}s time to run.")
        return result

    return wrapper


# This @performance decorator will check how long this function will take.
@performance
def long_time():
    print('1')
    for i in range(100000000):
        i * 5

@performance
def long_time2():
    print("2")
    for i in list(range(100000000)):
        i * 5


long_time()
long_time2()
