# Check whether a string is palindrome or not ? Do it with and without slicing 


from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"It took {end_time - start_time}s time to run.")
        return result

    return wrapper
# Do it using slicing

string = input("Enter a string : ")

@performance
def slicing_method(string):
    if string == string[::-1]:
        print("This is an palindrome string.")
    else:
        print("This is not an palindrome string.")


# Do it without slicing
@performance
def without_slicing(string):
    reverse_string = ""
    for alphabets in string:
        reverse_string =  alphabets + reverse_string
    if string == reverse_string:
        print("This is an palindrome string.")
    else:
        print("This is not an palindrome string.")

choose = int(input("By which method you want to check whether a string is palindrome or not \n1. Using slicing\n2. Without using slicing\nYour choice : "))
if choose == 1:
    slicing_method(string)
elif choose == 2:
    without_slicing(string)
else:
    print("Please choose either of these two methods.")