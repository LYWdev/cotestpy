#ccc19j1
applenum1  = int(input())
applenum2  = int(input())
applenum3  = int(input())
banananum1 = int(input())
banananum2 = int(input())
banananum3 = int(input())

apple_total = (applenum1*3)+(applenum2*2)+(applenum3*1)
banana_total = (banananum1*3)+(banananum2*2)+(banananum3*1)

if banana_total > apple_total :
  print('B')
elif banana_total < apple_total :
  print('A')
else :
  print('T')