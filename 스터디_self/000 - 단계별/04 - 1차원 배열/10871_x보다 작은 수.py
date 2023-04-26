n,x=map(int,input().split()) 
A=list(map(int,input().split())) # 수열 (정수 n개로 이루어진 수열)


for i in A:
    if i<x:
        print(i, end=' ')