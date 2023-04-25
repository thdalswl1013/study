x=int(input())
n=int(input())

cnt=0
for i in range(n):
    a,b=map(int,input().split())
    cnt+=(a*b)

if cnt==x:
    print("Yes")
else:
    print("No")