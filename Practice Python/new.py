"""
Q.1 Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""

# print("Twinkle, twinkle, little star,\n  How I wonder what you are!\n\tUp above the world so high,\n\tLike a dimond in the sky.\nTwinkle, twinkle, little star,\n  How I wonder what you are")

# Here backslash n (\n) print the the statement in the new line. 
# Here backslash t (\t) print the the statement in the new line with addition of a tab space at first.





"""
Q.2 Write a Python program to get the Python version you are using.
"""

# from sys import version # We import version from sys(system) 
# print("Python Version is :",version)




"""
Q.3 Write a Python program to display the current date and time.
"""

# import datetime
# date = datetime.date.today()
# now = datetime.datetime.now()
# print("Date is :",date)
# print("Time now is :",now)




"""
Q.4 Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

# radius = float(input("Enter the radius :"))
# pi = 3.14
# area = pi*radius*radius
# print("The area of",radius,"circle is :",area)




"""
Q.5 Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""

# firstname = input("Enter the first name : ")
# lastname = input("Enter the last name : ")

# #Option 1
# print(lastname+" "+firstname)

# #Option 2
# print(firstname[::-1]+" "+lastname[::-1])





"""
Q.6 Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
"""

# values = input("Enter some comma seperated numbers : ")
# list = values.split(",") # It will return a list (.split method use sep: and seperate all the ',' commas)
# print("List :",list)
# tuple = tuple(list)
# print("Tuple :",tuple)




"""
Q.7 Write a Python program to display the first and last colors from the following list. 

color_list = ["Red","Green","White" ,"Black"]
"""

# color_list = ["Red","Green","White","Black"]

# print(color_list[0],color_list[-1])




"""
Q.8 Write a Python program to display the examination schedule. (extract the date from exam_st_date)

exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""


exam_st_date = (11, 12, 2014)
print("The examination will be start from %i/ %i/ %i"%(exam_st_date))




"""
Q.9 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
"""
# It's answer is not 125 it's answer is 625 how?

# we are not doing this => 5*5*5 = 125 instead we are doing => 5*5*5 = 555 and same for others.

# n = int(input("Enter the number : "))
# a = ("%s"%(n))
# b = ("%s%s"%(n,n))
# c = ("%s%s%s"%(n,n,n))
# print(a+b+c)


"""
Q.10 Write a python program to print the documents of python built-in functions.
"""

# a = abs
# print(a.__doc__)

# print(abs.__doc__)


"""
Q.11 Write a Python program to print the following 'here document'. 

Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""

# For printing this type of string we need to use three doubles quotes each side. 
# print("""
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example""")


"""
Q.12 Python program to get the volume of sphere with radius 6.
"""

# radius = 6
# volume = 4/3 * 3.14 * (radius**3)
# print(f"The volume of {radius} radius is {volume}")


"""
Q.13 Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
"""

# seventeen = 17
# given_number = int(input("Enter a number : "))
# if given_number > 17:
# 	diffrence = given_number - seventeen
# 	print(abs(diffrence**2))
# else:
# 	diffrence = given_number - seventeen
# 	print(abs(diffrence))


"""
Q.14 Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
n = int(input("Enter a number :"))
print(near_thousand(n))