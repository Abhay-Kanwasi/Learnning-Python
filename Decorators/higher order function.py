# A function that accepts another function as it's argument


def greet(func):
    func()


# function 'greet' is a higher order function

def hello():
    print("Konichiwa")


greet(hello)

# Or it is a function that return another function

def greet(func):
    func()

def greet2():
    def func():
        return "How are you!"
    return func