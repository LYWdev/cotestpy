#ccc06j1
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())


if num1 == 1:
  bugerchoice=461 
elif num1 == 2:
  bugerchoice=431 
elif num1 == 3:
  bugerchoice=420 
else :
  bugerchoice=0 

if num2 == 1:
  sidechoice=100 
elif num2 == 2:
  sidechoice=57 
elif num2 == 3:
  sidechoice=70 
else :
  sidechoice=0  

if num3 == 1:
  drinkchoice=130 
elif num3 == 2:
  drinkchoice=160 
elif num3 == 3:
  drinkchoice=118 
else :
  drinkchoice=0 


if num4 == 1:
  dessert=167 
elif num4 == 2:
  dessert=266 
elif num4 == 3:
  dessert=75 
else :
  dessert=0 
total =str(dessert+drinkchoice+sidechoice+bugerchoice)
print("Your total Calorie count is "+total+".")