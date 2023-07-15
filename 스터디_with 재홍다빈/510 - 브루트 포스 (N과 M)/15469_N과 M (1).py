# "1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열" 조건을 만족하는
# 길이가 M인 수열을 모두 구하시오

n, m = list(map(int, input().split())) # 3, 1 
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
            
dfs()