try :
     num1 , num2 = eval(input("enter two numbers , sepereated by a conna :"))
     result= num1/num2
     print("Result is ",result)
except ZeroDivisionError :
    print(" Division ny zero is error")
except SyntaxError :
     print("comma is missing  . enter number seperated by comma like this 1 ,2")
except :
     print("wrong input")
else:
     print("no exceptions")
finally :
     print("tis will exeucte no matter what")