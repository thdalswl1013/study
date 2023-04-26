n=int(input())
arr=list(map(int,input().split())) #   2   4 -10  4  9
arr_sort=sorted(list(set(arr)))    # -10  -9   2  4


dictionary={}
for i in range(len(arr_sort)):
    dictionary[arr_sort[i]]=i

for i in arr:
    print(dictionary[i],end=' ')

# 시간초과
"""
n=int(input())
arr=list(map(int,input().split()))
arr_sort=sorted(list(set(arr)))

for i in arr:
    print(arr_sort.index(i), end=' ')

"""


# 시간초과
"""
n=int(input())
arr=list(map(int,input().split()))
arr_sort=sorted(list(set(arr)))

for i in range(n):
    for j in range(len(arr_sort)):
        if arr[i]==arr_sort[j]:
            print(j, end=' ')
            
"""