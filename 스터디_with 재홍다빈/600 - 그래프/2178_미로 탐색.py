from collections import deque

n, m = map(int, input().split()) 
graph=[]

for i in range(n):
    graph.append(list(map(int,input())))


dx=[0,0,1,-1]
dy=[1,-1,0,0]

queue=deque([(0,0)])

cnt=0

#BFS
while queue:
    x,y=queue.popleft()
    for i in range(4):
        nextX, nextY=x+dx[i], y+dy[i]
        if 0<=nextX<n and 0<=nextY<m:
            if graph[nextX][nextY]==1:
                queue.append((nextX, nextY))
                graph[nextX][nextY]=graph[x][y]+1

print(graph[n-1][m-1])