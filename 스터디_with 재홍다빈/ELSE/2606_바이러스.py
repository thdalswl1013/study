
n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크 상에서 직접 연결되어있는 컴퓨터 쌍의 수

#arr=[]
graph = [[]*n for _ in range(n+1)]

for i in range(m):
    x, y= map(int, input().split())
    #arr.append([x,y])
    graph[x].append(y)
    graph[y].append(x)

cnt=0
visited=[0]*(n+1)

def dfs(start): # 그래프 탐색 -> dfs 
    global cnt
    visited[start]=1

    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt+=1
            
dfs(1)
print(cnt)