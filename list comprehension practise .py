n = int(input("Enter a positive integer: "))

odds = [i for i in range(1, n) if i % 2 == 1]
evens = [i for i in range(1, n) if i % 2 == 0]

print("Odd numbers under", n, ":", odds)
print("Even numbers under", n, ":", evens)

fruits = ["apple", "banana", "mango", "grape", "orange"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("Capitalized fruits:", capitalized_fruits)
