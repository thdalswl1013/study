n,m=map(int,input().split())

arr=[0]*n
for x in range(n): # 1 2 3 4 5
    arr[x]=x+1

temp=0
for x in range(m):
    i,j=map(int,input().split())
    temp=arr[i-1]
    arr[i-1]=arr[j-1]
    arr[j-1]=temp
    
for i in range(len(arr)):
    print(arr[i], end=' ')