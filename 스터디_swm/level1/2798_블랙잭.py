n, m =map(int, input().split())
n_list= list(map(int, input().split()))

# m을 넘지 않으면서, m에 최대한 가까운 세장의 합

result=0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if n_list[i] + n_list[j] + n_list[k] <= m:
                result=max(result, n_list[i] + n_list[j] + n_list[k])
                
print(result)