T=int(input())

def dfs(V):
    visited[V]=1  # 방문한 곳 1로 표시
    next=arr[V]
    if visited[next]==0: # next가 아직 방문하지 않은 곳인 경우
        dfs(next)

for i in range(T):
    result = 0
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)

    for i in range(1, N+1):
        if visited[i]==0:
            dfs(i)
            result+=1
    print(result) #순열 사이클의 개수



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