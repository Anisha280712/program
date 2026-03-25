
test_dict = {
    'Codingal': 3,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1
}


print("Test Dictionary:", test_dict)

value = input("Enter the value you want to check the frequency of: ")

if value.isdigit():
    value = int(value)

frequency = list(test_dict.values()).count(value)

print("Frequency:", frequency)
