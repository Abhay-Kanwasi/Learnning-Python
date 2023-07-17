import math
import time 

center_x = int(input("Enter the center of x : "))
center_y = int(input("Enter the center of y : "))
circle_radius = int(input("Enter the circle radius : "))
point_x = int(input("Enter the value of x point : "))
point_y = int(input("Enter the value of y point : "))

print("\nCalculating....")
time.sleep(2)
distance = math.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)
print("Distance is",round(distance,2))
time.sleep(2)
print("\nCalculating...")
time.sleep(2)
if distance < circle_radius:
    print("The point lies inside the circle.")
else:
    print("The point lies outside the circle.")
