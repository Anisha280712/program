a=10
b=20
c=30
avg=(a+b+c)/3
print("the avg of all the 3 speed is:",avg)
if avg>a and avg>b and avg>c:
    print("average is greater than a ,b,c")
elif avg>a:
    print("average is greater than a")
elif avg>b:
    print("average is greater than b")
elif avg>c:
    print("avgrage is greater than c")

else:
    print ("invalid")