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
    for i in range(100000000):
        i * 5


long_time()
