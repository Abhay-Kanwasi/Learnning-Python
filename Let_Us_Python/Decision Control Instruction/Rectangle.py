length = int(input("Enter the length of rectangle : "))
breadth = int(input("Enter the breadth of rectangle : "))
perimeter_of_reactangle = 2*(length + breadth)
area_of_reactangle = length * breadth
if area_of_reactangle > perimeter_of_reactangle:
    print("Area of reactangle is greter than it's perimeter.")
else:
    print("Area of reactangle is greter not than it's perimeter.")