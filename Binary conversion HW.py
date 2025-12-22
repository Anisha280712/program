num = int(input("Enter a decimal number: "))
original_num = num
if num == 0:
    binary = "0"
else:
    binary = ""  
while num > 0:
        remainder = num % 2  
        binary = str(remainder) + binary
        num = num // 2   
print("Decimal:", original_num)
print("Binary:", binary)