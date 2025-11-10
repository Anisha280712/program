cp=float(input("please enter the cost price:"))
sp=float(input("please enter the selling price:"))
if (sp>cp):
  profit=sp-cp
  print("total profit =",profit)  
else:
  print("no profit")