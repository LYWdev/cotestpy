#ccc07j1
#whoisinthemiddle
num1=int(input())
num2=int(input())
num3=int(input())

#middle이  num1,2,3인 경우로 나눠야함
#middle이 num1인 경우 즉 2보다 작고 3보다 크거나 3보다 작거나 2보다 클경우

#// [num2 < num1 < num3 일 때] or [num3 < num1 < num2 일 때]
if ((num1 > num2) and (num1 < num3)) or ((num1 > num3) and (num1 < num2)):
  middle = num1
  print(middle)

# [num3 < num2 < num1 일 때] or [num1 < num2 < num3 일 때] 
elif ((num2 > num3) and (num2 < num1)) or ((num2 > num1) and (num2 < num3)):
  middle = num2
  print(middle)
# [num3 < num2 < num1 일 때] or [num1 < num2 < num3 일 때] 
else:
  middle = num2
  print(middle)