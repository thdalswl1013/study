n,m=map(int,input().split())
arr=list(map(int,input().split()))

"""
입력 받은 배열을 누적 합 배열로 바꾸고,
구하려 하는 구간 i, j에 해당하는 두 원소의 차를 구해 그 구간의 합을 구하는 방식
"""

for i in range(n-1):
    arr[i+1]+=arr[i] # 5 9 12 14 15

arr=[0]+arr # 0 5 9 12 14 15

for i in range(m):
    a,b=map(int,input().split())
    print(arr[b]-arr[a-1])


# 시간 초과 -> time complexity: O(n^2)
"""
n,m=map(int, input().split())

n_num=list(map(int,input().split()))


for i in range(m):
    sum=0

    a,b=map(int, input().split())

    if a==b:
        sum=n_num[a-1]
        
    else:
        for i in range(a, b+1):
            sum+=n_num[i-1]

    print(sum)


"""