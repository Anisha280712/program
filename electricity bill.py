unit=int(input("please enter the number of units you consumed : "))
if unit<50:
    amount=unit*2.60
    tax=25
elif unit<=100:
    amount=130+((unit-50)*3.25)
    tax=35
elif unit<=200:
    amount=130+162.50+((unit-100)*5.26)
    tax=45
else:
    amount=130+162.5+526+((unit-200)*8.45)
    tax=75
totalamount=amount+tax
print("TOTAL AMOUNT =",totalamount)
