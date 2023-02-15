n=int(input())

length=list(map(int, input().split())) # 2, 3, 1
weight=list(map(int, input().split())) # 5, 2, 4, 1

# 제일 싼 곳 찾아서 거기서 많이 넣기 
result=0
min = weight[0] # 5

for i in range(len(length)):

    if min>weight[i]: # 더 싼 가격이 나오기 전에는 현재 가격으로 충전함
        min=weight[i]

    result += min * length[i] # 제일 처음에는 weight[0] * length[0]

print(result)

# SOL2
"""
n=int(input())

length=list(map(int, input().split())) # 2, 3, 1
weight=list(map(int, input().split())) # 5, 2, 4, 1

result = weight[0] * length [0]

min=weight[0]

for i in range(1, len(length)):
    if min>weight[i]:
        min = weight[i]
    result += min * length[i]

print(result)
"""