# 값을 1로 만들기 -> DP문제 


# Bottom_Up 방식 풀이
n = int(input())
dp = [0] * (n+1) # 인덱스 숫자가 1이 되는데 필요한 연산 최소 개수

for i in range(2, n+1):
    dp[i]= dp[i-1] + 1 # 1을 빼는 연산

    if i%2==0: # 2로 나누어 떨어질 때, 2로 나누는 연산
        dp[i] = min(dp[i], dp[i//2]+1)

    if i%3==0: # 3으로 나누어 떨어질 때, 3으로 나누는 연산
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])