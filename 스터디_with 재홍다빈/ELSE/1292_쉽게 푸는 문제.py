a,b= map(int,input().split())

arr = []
for i in range(46):
    for j in range(i):
        arr.append(i)

#print(arr)

sum=0
for i in range(a, b+1):
    sum+=arr[i-1]

print(sum)