# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Given:

class Vehical:

    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage
    
class Bus(Vehical):
    pass

School_Bus = Bus("Rajesh Memorial Children Academy",50,20)

print("Name :",School_Bus.name,"Speed :",School_Bus.speed,"Mileage :",School_Bus.mileage)