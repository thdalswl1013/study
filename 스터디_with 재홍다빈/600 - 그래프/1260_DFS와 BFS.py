from collections import deque

n, m, v = list(map(int, input().split()))
graph=[[False]*(n+1) for _ in range(n+1)]


for i in range(m):
    a, b = map(int, input().split())

    graph[a][b]=True
    graph[b][a]=True

visited1=[False]*(n+1) # DFS 방문 기록
visited2=[False]*(n+1) # BFS 방문 기록


def DFS(v):
    visited1[v]=True
    print(v, end=" ")

    for i in range(1, n+1):
        if not visited1[i] and graph[v][i]:
            DFS(i)

def BFS(v):
    q=deque([v])
    visited2[v]=True

    while q:
        v=q.popleft()
        print(v, end=" ")

        for i in range(1, n+1):
            if not visited2[i] and graph[v][i]:
                q.append(i)
                visited2[i]=True
    

DFS(v)
print()
BFS(v)