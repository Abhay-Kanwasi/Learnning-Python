def hello(func):
    func()


def start():
    print("I'm coming bro!!")


message = hello(start)
print(message)

# Ability of functions to act like variable is essential for decorators


# A decorator supercharges our function it is simply a function that wraps another function and enhances it
