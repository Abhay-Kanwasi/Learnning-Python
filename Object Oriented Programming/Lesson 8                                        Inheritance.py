# Inheritence : Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

# There are 3 types of inheritance :
# 1. Single Level Inheritance 
# 2. Multi Level Inheritance
# 3. Multiple Level Inheritance


# Let's discuss..

# 1. Single Level Inheritance

# In single level inheritence one class(A) inherit properties from another one class(B).

class A:

    def feature1(self):
        print("Feature 1 is working.")

    def feature2(self):
        print("Feature 2 is working.")

class B(A): # It means B inherit from A.

    def feature3(self):
        print("Feature 3 is working.")

    def feature4(self):
        print("Feature 4 is working.")

a = A() # We created object a.
b = B() # We created object b. 

# Now if you try :

# Object a only have :-
a.feature1()
a.feature2()

# Object b can access a because it inherits a. (b not only it can access it features It can access a as well.)
b.feature1()
b.feature2()
b.feature3()
b.feature4()





# 2. Multilevel Inheritence

# In multilevel inheritence 

class A:

    def feature1(self):
        print("Feature 1 is working.")

    def feature2(self):
        print("Feature 2 is working.")

class B(A): # It means B inherit from A.

    def feature3(self):
        print("Feature 3 is working.")

    def feature4(self):
        print("Feature 4 is working.")

class C(B): # It means C inherit from B.

    def feature5(self):
        print("Feature 5 is working.")

a = A() # We created object a.
b = B() # We created object b.
c = C() # We created object c.

# Now if you try :

# Object a only have :-
a.feature1()
a.feature2()

# Object b can access a because it inherits a. (b not only it can access it features It can access a as well.)
b.feature1()
b.feature2()
b.feature3()
b.feature4()

# Object c can access all the b features because it inherits b.
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()



# 3. Multilevel Inheritence


class A:

    def feature1(self):
        print("Feature 1 is working.")

    def feature2(self):
        print("Feature 2 is working.")

class B: 

    def feature3(self):
        print("Feature 3 is working.")

    def feature4(self):
        print("Feature 4 is working.")

class C(A,B): # It means C inherit from B.

    def feature5(self):
        print("Feature 5 is working.")

a = A() # We created object a.
b = B() # We created object b.
c = C() # We created object c.

# Now if you try :

# Object a only have :-
a.feature1()
a.feature2()

# Object b only have :-
b.feature3()
b.feature4()

# Object c can access all the b features because it inherits b.
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()

 

