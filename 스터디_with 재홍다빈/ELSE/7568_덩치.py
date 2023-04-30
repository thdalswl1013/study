n=int(input())
arr=[]
for i in range(n):
    x,y=map(int, input().split())
    arr.append([x,y])

result=[]
for i in range(n):
    cnt=0
    for j in range(n):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            cnt+=1
    result.append(cnt+1)

for i in range(n):
    print(result[i], end=' ')