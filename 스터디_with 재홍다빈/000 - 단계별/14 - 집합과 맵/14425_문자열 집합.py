n,m=map(int,input().split())

s=set()
for i in range(n):
    s.add(input())

cnt=0
for i in range(m):
    t=input()

    if t in s:
        cnt+=1

print(cnt)


# 시간초과
"""
n,m=map(int,input().split())

s=[]
for i in range(n):
    s.append(input())

check=[]
for i in range(m):
    check.append(input())
    

cnt=0
for i in range(n):
    for j in range(m):
        if s[i]==check[j]:
            cnt+=1

print(cnt)

"""