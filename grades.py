print("enter marks obtained in 5 subjects")
mark1=int(input("enter marks:"))
mark2=int(input("enter marks:"))
mark3=int(input("enter marks:"))
mark4=int(input("enter marks:"))
mark5=int(input("enter marks:"))
total=mark1+mark2+mark3+mark4+mark5
average=total/5

if average>=91 and average<=100:
    print("A1")
elif average>=81 and average<91:
    print("A2")
elif average>=71 and average<81:
    print("B1")
elif average>=61 and average<71:
    print("B2")
elif average>=51 and average<61:
    print("C1")
elif average>=41 and average<51:
    print("C2")
elif average>=33 and average<41:
    print("D")
elif average>=21 and average<33:
    print("E1")
elif average>=0 and average<21:
    print("E2")
else:
    print("invalid input")