m=int(input())
n=int(input())

cnt=0
arr=[]
for i in range(m, n+1):
    for j in range(1, n):
        if i//j==j and i%j==0:
            arr.append(i)
            cnt+=i
            min=arr[0]

for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]


if cnt==0:
    print(-1)

else:
    print(cnt)
    print(min)
