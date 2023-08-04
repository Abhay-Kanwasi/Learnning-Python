# Create our own decorator
def my_decorator(func):
    def wrap_func():
        print("************")
        func()
        print("************")

    return wrap_func


# @my_decorator
def hello():
    print("Hello")


# What actually happening when @my_decorator used
hello_new = my_decorator(hello)
hello_new() # Now hello_new is equal to wrap func()


@my_decorator
def bye():
    print("Bye")


# hello()
bye()
