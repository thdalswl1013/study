m=int(input())
n=int(input())

def decimal(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

arr=[]
for i in range(m, n+1):
    if i>1: # i>1 때문에 틀렸었음!
        if decimal(i):
            arr.append(i)


if len(arr)>0:
    print(sum(arr))
    print(arr[0])

else:
    print(-1)