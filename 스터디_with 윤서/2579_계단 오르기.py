# 계단 오르기 -> DP 문제

n = int(input()) # 6
stair = [] # 10, 20, 15, 25, 10, 20
dp = [0] * n

for i in range(n):
    stair.append(int(input()))

if len(stair) <= 2:
    print(sum(stair))

else:
    dp[0]=stair[0] # 첫째 계단
    dp[1]=stair[0]+stair[1] # 둘째 계단

    for i in range(2, n): # 셋째 계단~
        dp[i]= max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
        """
        # dp[i-3]+stair[i-1]+stair[i]: i-3까지의 계단 점수 최댓값과 i-1, i 계단의 합.
        # dp[i-2]+stair[i]: i-2까지의 계단 점수 최댓값과 i 계단의 합.
        
        -> 3번째 계단부터 2계단을 연속으로 걸었을 때와, 1계단을 건너뛴 것을 비교
        """

    print(dp[-1])