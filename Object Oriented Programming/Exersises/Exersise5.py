# Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

# Use the following code for this exercise.

class Vehicle:

    def __init__(self, name, max_speed, mileage,color="white"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

Vehical_1 = Bus("RMCA Bus",60,20,"red")
Vehical_2 = Car("ABYCUS",280,15) # Here I don't give the color so it will take the default value.

print("Vehical Name :",Vehical_1.name,"\nMax Speed :",Vehical_1.max_speed,"\nMileage :",Vehical_1.mileage,"\nColor :",Vehical_1.color)

print("\n")

print("Vehical Name :",Vehical_2.name,"\nMax Speed :",Vehical_2.max_speed,"\nMileage :",Vehical_2.mileage,"\nColor :",Vehical_2.color)