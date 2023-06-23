n = input()

comp = len(n) - 1

answer = 0

for i in range(comp):
    answer += 9 * (10 ** i) * (i + 1)
    i += 1
answer += ((int(n) - (10 ** comp)) + 1) * (comp + 1)

print(answer)



# 틀린 풀이
"""
cnt=0
for i in range(n):
    if i<10:
        cnt+=1
    elif 10<=i and i<100:
        cnt+=2
    elif 100<=i and i<1000:
        cnt+=3
    elif 1000<=i and i<10000:
        cnt+=4
    elif 10000<=i and i<100000:
        cnt+=5
    elif 100000<=i and i<1000000:
        cnt+=6
    elif 1000000<=i and i<10000000:
        cnt+=7
    elif 10000000<=i and i<100000000:
        cnt+=8
    else:
        cnt+=9
    
print(cnt)

"""

# 메모리 초과
"""
n=int(input())
arr=[]

for i in range(n):
    arr.append(i+1)


sen="".join(str(_) for _ in arr)
print(len(sen))

"""
