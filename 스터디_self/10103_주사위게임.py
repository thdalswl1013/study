n=int(input())
x=100
y=100
for i in range(n):
    a,b=map(int,input().split())

    if a<b:
        x-=b
    elif a>b:
        y-=a

print(x)
print(y)
