n=int(input())
n_list=list(map(int, input().split()))
n_list.sort()

m=int(input())
m_list=list(map(int, input().split()))

def binarySearch(num, bound, start, end):    
    while start<end:
        middle = (start+end)//2

        if bound==0:
            if n_list[middle] < num:
                start = middle + 1
            else:
                end = middle

        else:
            if n_list[middle] <= num:
                start = middle + 1
            else:
                end = middle
    return end 
            
result=[]

for i in m_list:
    result.append(binarySearch(i, 1, 0, n) - binarySearch(i, 0, 0, n))

for i in range(len(result)):
    print(result[i], end=' ')

# 시간 초과
"""
arr=[]

for i in range(m):
    result=0
    for j in range(n):
        if n_list[j]==m_list[i]:
            result+=1
    arr.append(result)

print(arr)
"""

# 시간 초과
"""
for i in range(m):
    result=0
    for j in range(n):
        if n_list[j] == m_list[i]:
            result+=1

    print(result, end=' ')

"""


