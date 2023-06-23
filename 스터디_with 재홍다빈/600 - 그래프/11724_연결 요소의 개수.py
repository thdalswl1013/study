import sys
sys.setrecursionlimit (10000)

def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n+1)
cnt = 0


for i in range(1, n + 1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]: # 만약 해당 정점이 연결된 그래프가 없다면
            cnt += 1
            visited[i] = True 

        else:  # 연결된 그래프가 있다면
            dfs(i) # dfs탐색을 돈다.
            cnt += 1

print(cnt)
