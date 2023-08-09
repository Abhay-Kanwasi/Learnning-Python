# num = int(input('Enter the number : ')); print(num)



def example_function(arg1, *args, **kwargs):
    print("Regular argument:", arg1)
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

example_function("Hello", 2, 3, 4, 5, 6,('a','b'),[2,3,4], name="Alice", age=25)
