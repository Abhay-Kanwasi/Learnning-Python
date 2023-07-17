# If the three of a triangle are entered through the keyboard write a program to check whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater than the largest of the three sides.

side1 = int(input("Enter the first side : "))
side2 = int(input("Enter the second side : "))
side3 = int(input("Enter the third side : "))

if side1+side2>=side3 and side3+side1>=side2 and side2+side3>=side1:
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")  