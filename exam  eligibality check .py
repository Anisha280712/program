medicalcause=input("Do you have a medical cause y or n :")
if medicalcause=="y" :
    print("allowed")
else:
    attendance=int(input("enter the attendance of the student:"))
    if attendance>=75:
        print("allow")
    else:
        print(" not allowed")


