x=input() # x==Python programming
x=x.capitalize() # 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환한다. -> x==Python programming
y=x.split() # y==['Python', 'programming']

print(y[0][::2], end='*') 
print(y[1][3:6])

 # Pto*gra
