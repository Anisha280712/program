amount=int(input("enter the amount:"))
note100=amount//100
note50=(amount%100)//50
note10=((amount%100)%50)//10
print("notes of 100 pounds:",note100)
print("notes of 50 pounds:",note50)
print("notes of 10 pounds:",note10)