import time
from triangle import Triangle_Properties

side1 = int(input("Enter the side1 : "))
side2 = int(input("Enter the side2 : "))
side3 = int(input("Enter the side3 : "))

print("\nCalculating the sides...")
time.sleep(2)
print(f"Given sides are : {side1},{side2},{side3}\nTriangle is isosceles : {Triangle_Properties.triangle_is_isosceles(side1,side2,side3)}\n")
time.sleep(2)

print(f"Given sides are : {side1},{side2},{side3}\nTriangle is scalene : {Triangle_Properties.triangle_is_scalene(side1,side2,side3)}\n")
time.sleep(2)

print(f"Given sides are : {side1},{side2},{side3}\nTriangle is equilateral : {Triangle_Properties.triangle_is_equilateral(side1,side2,side3)}\n")
time.sleep(2)

print(f"Given sides are : {side1},{side2},{side3}\nTriangle is valid using sides : {Triangle_Properties.valid_triangle_by_sides(side1,side2,side3)}\n")
time.sleep(2)

print("#############################################################")
angle1 = int(input("Enter the angle1 : "))
angle2 = int(input("Enter the angle2 : "))
angle3 = int(input("Enter the angle3 : "))

print("\nCalculating the angles...")
time.sleep(2)
print(f"Given angles are : {angle1},{angle2},{angle3}\nTriangle is valid using angles : {Triangle_Properties.valid_triangle_by_angles(angle1,angle2,angle3)}")

