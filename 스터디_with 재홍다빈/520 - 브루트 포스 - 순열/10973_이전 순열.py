"""
n=int(input())
arr=list(map(int,input().split()))

n_arr=[]
for i in range(n):
    n_arr.append(i+1)


if n_arr==arr:
    print(-1)
"""

n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if arr[i - 1] > arr[i]:
        for j in range(n - 1, 0, -1):
            if arr[i - 1] > arr[j]:
                arr[i - 1], arr[j] = arr[j], arr[i - 1]
                arr = arr[:i] + sorted(arr[i:],reverse=True)
                print(*arr)
                exit()
print(-1)