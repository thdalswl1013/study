#어렵따,,

n=int(input())
n_list=list(map(int, input().split()))

dp=[]
for i in range(n):
    dp.append(1)

for i in range(1, n):
    dp_max=0

    for j in range(i):
        if n_list[j]<n_list[i]:
            dp_max=max(dp_max, dp[j])
    
    dp[i]=dp_max+1

print(max(dp))