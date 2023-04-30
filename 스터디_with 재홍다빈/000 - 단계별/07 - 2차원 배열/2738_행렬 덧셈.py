n,m=map(int,input().split())

A=[]
B=[]

for i in range(n):
    i=list(map(int,input().split()))
    A.append(i)

for i in range(n):
    i=list(map(int,input().split()))
    B.append(i)

for i in range(n):
    for j in range(m):
        print(A[i][j]+B[i][j], end=' ')
    print()