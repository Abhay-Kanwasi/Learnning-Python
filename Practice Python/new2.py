
with open('text.txt','w') as file:
    file.write("blah blah")


file = open('text.txt', 'w')
file.write('toislk')
file.close()



def topfour():
    yield 1
    yield 2
    yield 3


values = topfour()
print(values.__next__())
print(type(values))
for i in values:
    print(i)


a = (2) # integer
b = (2,) # tuple



# read
with open('texttxt','r') as file:
    content = file.read()

# readline

# readlines




# ** kwargs
def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))

# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

# *args 
def myFun(arg1, *argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# use case of decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# iterator
num = [2,3,4]
num_iterator = iter(num)

# __next__
# print(num_iterator.__next__())
# print(num_iterator.__next__())
print(num_iterator.__next__())

# for loop
for digit in num_iterator:
    print(digit)




# method overriding 
class Parent:
    def show(self):
        print("Parent's show method")

class Child(Parent):
    pass

obj1 = Parent()
obj2 = Child()

obj1.show()  # Output: "Parent's show method"
obj2.show()  # Output: "Child's show method"


#list compehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_even_numbers = [x ** 2 for x in numbers if x % 2 == 0]

print(squared_even_numbers)  # Output: [4, 16, 36, 64, 100]

# ternery operator in python
age = 19
elgibility = "You are not eligible for vote" if age<18 else "You can vote"
print(elgibility)

# list comprehension 

a = [2,3,4,5,1,6]
b = [num for num in a if num%2==0]
print(b)

# Constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating instances using the constructor
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name, person1.age)  # Output: Alice 25
print(person2.name, person2.age)  # Output: Bob 30
