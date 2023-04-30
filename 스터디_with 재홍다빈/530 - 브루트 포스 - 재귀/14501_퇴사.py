"""
dp: 하나의 문제는 단 한 번만 풀게 하는 알고리즘 
- 큰 문제는 작은 문제로 나눌 수 있다.
- 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
"""


# T: 상담을 완료하는데 걸리는 시간
# P: 상담을 했을 때 받을 수 있는 금액

n=int(input())
t=[]
p=[]
dp=[]

for i in range(n):
    t_i, p_i = list(map(int, input().split()))
    t.append(t_i)
    p.append(p_i)
    dp.append(p_i)

dp.append(0) # dp 맨 뒤에 0 값을 추가

for i in range(n-1, -1, -1):
    if t[i]+i > n: # 상담이 끝나는 날이 n을 넘어가면, 일을 맡을 수 x
        dp[i] = dp[i+1]

    else: # 상담이 끝나는 날이 n을 넘어가지 않는다면
        dp[i]=max(dp[i+1], p[i] + dp[i+t[i]]) # p[i] + dp[i+t[i]]: 현재 일을 맡았을 때 들어오는 보상 + 현재 일을 끝냈을 때 쌓여있는 보상
                                              # dp[i+1]          : 일을 맡지 않을 경우의 보상
    
print(dp[0])

