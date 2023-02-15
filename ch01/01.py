# word count
##String
#.upper()는 대문자로 전환하는 메소드
# 변수와 변수할당은 아래와 같이함.
word ='   aabaaabacbaa word count'
print(word.upper())

#.strip()는 공백 제거
print(word.strip())
stripedword=word.strip()

print("stripedword:"+ str(stripedword.count(' ')+1))
#.()count는 문자열안에 arg 개수를 알려줌
# args가 겹칠 경후 첫 번째료 발견된 것만 카운트
print(word.count(' ')+1)

print("-"*30)
# Operator
# 사칙연산 전부 가능
print(1+1)
print(2-1)
print(3*1)
# //는 나머지 버림.
print(5//8)
print(2%8)


print(""*30) 
print("-"*30)