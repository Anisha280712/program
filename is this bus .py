class vehicle :
    def __init__ (self ,name,max_speed , mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage
class Bus(vehicle):
     pass
School_Bus = Bus ("School Volvo",180,12)
print("vehicle name :", School_Bus.name , "speed:",School_Bus.max_speed,"mileage:",School_Bus.mileage)