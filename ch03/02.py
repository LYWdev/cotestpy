#coci06c5p1 
#Chapter3 반복문 한정 루프

# secret_word = "OliVe"

# #Nesting
# #isupper()는 upper판한해서 bool리턴하는 함수
# for char in secret_word:
  # if char.isupper():
    # print("대문자 :"+char)

letter = "ABC"
digits = "123"
print(letter+digits)
for char in letter:
  for num in digits:
    print(char+num)
