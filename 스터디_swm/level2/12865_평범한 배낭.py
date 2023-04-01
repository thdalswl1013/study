"""
DP's Knapsack problem
-> x축엔 가방 1~K 까지의 무게, y축은 물건 N개 개수만큼의 배열 
"""

n,k=list(map(int, input().split()))

stuff = [ [0, 0] ]
dp = [ [0 for _ in range(k+1)] for _ in range(n+1) ] # dp[i][j]: 처음부터 i번째까지의 물건을 살펴보고, 배낭 용량이 j일 때 배낭에 들어간 물건의 가치값의 최대값

for _ in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        weight= stuff[i][0] # i번째 물건의 무게
        value = stuff[i][1] # i번째 가치

        """
        용량이 j인 배낭에 i번째 물건을 넣지 않았을 때: dp[i-1][j]
        용량이 j인 배낭에 i번째 물건을 넣었을 때: value + dp[i-1][j-weight]
        """

        if j < weight: 
            dp[i][j]=dp[i-1][j]  
        
        else: 
            dp[i][j]=max(dp[i-1][j], value+dp[i-1][j-weight]) # dp[이전물건][현재가방무게] vs 현재물건가치+dp[이전물건][현재가방무게-현재물건무게]

print(dp[n][k]) # 모든 물건 1~n을 살펴보고, 배낭 용량이 k일 때 이 배낭에 들어가 있는 물건들의 가치합의 최대값