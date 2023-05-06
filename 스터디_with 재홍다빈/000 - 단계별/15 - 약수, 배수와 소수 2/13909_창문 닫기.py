
# 메모리 초과
"""
n=int(input())
arr = [0] * (n+1)
for i in range(1, n+1): # 열려있으면 1, 닫혀있으면 0
    for j in range(i, n+1, i):
        if arr[j] == 0:
            arr[j] = 1
        else:
            arr[j] = 0

print(arr.count(1))

"""
n=int(input())
r=0
c=1
while(c<=n):
    r+=1
    c=(r+1)**2
print(r)