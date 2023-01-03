n=int(input())

arr=[0]*n # arr[i]=j : queen을 (i, j) 위치에 놓겠다는 뜻
ans=0

def is_promising(x):
    for i in range(x):
        if arr[x]==arr[i]:
            return False
        if abs(arr[x]-arr[i])==abs(x-i):
            return False
    return True

def n_queens(x):
    global ans
    
    if x==n:
        ans+=1

    else:
        for i in range(n):
            arr[x]=i

            if is_promising(x):
                n_queens(x+1)
n_queens(0)
print(ans)

            



 
