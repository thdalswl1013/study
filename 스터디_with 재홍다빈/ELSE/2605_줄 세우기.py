n=int(input())
arr=list(map(int, input().split()))

result=[]

for i in range(n):
    result.insert(i - arr[i], i+1)

for i in result:
    print(i, end = ' ')