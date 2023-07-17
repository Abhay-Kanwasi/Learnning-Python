# Program to receive radius of a circle, and length and breadth of a reactangle in one call to input(). Calculate and print the circumference of circle and perimeter of rectangle.

radius = int(input("Enter the radius of the circle : "))
length = int(input("Enter the length of the circle : "))
breadth = int(input("Enter the breadth of the circle : "))

circumference = 2 * 3.14 * radius
perimeter = 2 * (length + breadth)

print(f'Circumference of circle : {circumference}')
print(f'Perimeter of circle : {perimeter}')