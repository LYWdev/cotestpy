#ccc15j2
#CCandCheesekun

strinput=str(input())
happy=':-)'
sad=':-('
happy_count=strinput.count(happy)
sad_count=strinput.count(sad)

if happy_count == 0 and sad_count==0:
  print("none")
elif happy_count == sad_count:
  print("unsure")
elif happy_count > sad_count:
  print("happy")
#happy_count > sad_count:
else :
  print("sad")