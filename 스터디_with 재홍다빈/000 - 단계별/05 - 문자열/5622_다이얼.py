alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alphabet :  
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in word :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                time += alphabet.index(unit) +3  # time = time + index +3
print(time)



"""
arr=list(input())
print(arr)

cnt=0
for i in arr:
    if i=='A' or i=='B' or i=='c':
        cnt+=3
    elif i=='D' or i=='E' or i=='F':
        cnt+=4
    elif i=='G' or i=='H' or i=='I':
        cnt+=5
    elif i=='J' or i=='K' or i=='L':
        cnt+=6
    elif i=='M' or i=='N' or i=='O':
        cnt+=7
    elif i=='P' or i=='Q' or i=='R' or i=='S':
        cnt+=8
    elif i=='T' or i=='U' or i=='V':
        cnt+=9
    elif i=='W' or i=='X' or i=='Y' or i=='Z':
        cnt+=10

print(cnt)
"""