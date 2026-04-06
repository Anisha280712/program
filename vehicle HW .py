class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "BMW max speed is 250 km/h"


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "Ferrari max speed is 340 km/h"


# Polymorphism in action
def show_car_details(car):
    print("Fuel type:", car.fuel_type())
    print("Max speed:", car.max_speed())
    print("-" * 30)


bmw_car = BMW()
ferrari_car = Ferrari()

show_car_details(bmw_car)
show_car_details(ferrari_car) 
