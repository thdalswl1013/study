n, m=map(int,input().split())

listen=[]
see=[]

for i in range(n):
    listen.append(input())

for i in range(n+2, n+m+2):
    see.append(input())

#print(listen): ['ohhenrie', 'charlie', 'baesangwook']
#print(see): ['obama', 'baesangwook', 'ohhenrie', 'clinton']

listen_see=list(set(listen) & set(see))
listen_see.sort()

print(len(listen_see))

for i in range(len(listen_see)):
    print(listen_see[i])


# 시간초과 SOL
"""
cnt=0
listen_see=[]
for i in range(n):
    for j in range(m):
        if listen[i]==see[j]:
            cnt+=1
            listen_see.append(listen[i])
listen_see.sort()
     
print(cnt)

for i in range(cnt):
    print(listen_see[i])
"""