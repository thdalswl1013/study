# 런타임 에러
""" 
def dfs(x):
    visited[x]=True # 방문 체크
    number=number[x] # 다음 방문 장소
    
    if not visited[number]: # 방문하지 않았다면
        dfs(number) # 재귀함수 호출 


t=int(input())
for i in range(t):
    n=int(input())
    arr=[0]+list(map(int,input().split()))
    
    visited=[True] + [False]*n
    
    result=0
    for j in range(1, n+1):
        if not visited[i]:
            dfs(i)
            result+=1
    print(result)
"""