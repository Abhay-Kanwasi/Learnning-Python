# Check distance between two points : under root (x1-x2)^2 + (y1-y2)^2

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def calculate_distance_with(self, point2):
        distance = ((self.x - point2.x)**2 + (self.y - point2.y)**2) ** 0.5
        return distance

# instance of the class

point1 = Point(1,2)
point2 = Point(4,6)

distance = point1.calculate_distance_with(point2)
print(f'Distance between point1 and point2 is  {distance}')