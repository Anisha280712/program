try:
    age_input = input("Enter your age: ")
    age = int(age_input)  # Try converting to integer
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
except ValueError:
    print("ValueError: Please enter a valid whole number for age.")
