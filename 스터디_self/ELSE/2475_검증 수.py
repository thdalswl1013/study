arr=list(map(int, input().split()))

result=0
for i in range(5):
    result+=arr[i]*arr[i]
print(result%10)