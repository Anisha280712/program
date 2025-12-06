def power_calculator(base, max_power):
   
    for p in range(1, max_power + 1):
        result = base ** p
        print(f"{base}^{p} = {result}")


try:
    base = float(input("Enter the base number: "))
    max_power = int(input("Enter how many powers to compute (n): "))
    if max_power <= 0:
        print("Please enter a positive integer for n.")
    else:
        power_calculator(base, max_power)
except ValueError:
    print("Invalid input. Use numbers for base and an integer for n.")