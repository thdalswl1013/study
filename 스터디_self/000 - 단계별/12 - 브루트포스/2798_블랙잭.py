n,m=map(int,input().split())
arr=list(map(int,input().split()))
sum_arr=sum(arr)

result=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if result<arr[i]+arr[j]+arr[k]<=m:
                result=arr[i]+arr[j]+arr[k]
print(result)
