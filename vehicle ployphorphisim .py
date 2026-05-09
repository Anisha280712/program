class BMW:
    def fuel_type(self):
        return "Diesel"

    def max_speed(self):
        return "BMW max speed: 240 km/h"


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "Ferrari max speed: 340 km/h"


# Polymorphism in action
def show_car_details(car):
    print(car.fuel_type())
    print(car.max_speed())


# Objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Calling the same function with different objects
show_car_details(bmw_car)
print()
show_car_details(ferrari_car)
