class Dog:
    
    animal = "dog"

    def __init__(self, breed, colour):
        
        self.breed = breed
        self.colour = colour

dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

print("Dog 1 Details:")
print("Animal:", Dog.animal)
print("Breed:", dog1.bbreed)
print("Colour:", dog1.colour)

print("\nDog 2 Details:")
print("Animal:", Dog.animal)
print("Breed:", dog2.breed)
print("Colour:", dog2.colour)

