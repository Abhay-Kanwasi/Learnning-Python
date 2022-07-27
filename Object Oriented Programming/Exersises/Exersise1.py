# Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:

    def __init__(self,max,mil):
        self.maxspeed = max
        self.mileage = mil
    
Model1 = Vehicle(280,40)

print(Model1.maxspeed,Model1.mileage)