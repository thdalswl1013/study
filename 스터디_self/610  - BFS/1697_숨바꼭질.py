"""
처음 수빈이의 위치 n에서 동생의 위치 k로 가는 최단 시간 찾기 -> DFS or BFS

기존 위치에서 이동 가능한 위치: X-1, X+1, 2*X  = 노드가 3개로 펼쳐져 나갈 수 있다 
                                             = Queue에 append할 아이템이 3가지이다

최대, 최소 값이 존재하므로 X-1, X+1, 2*X 값이 범위를 넘어가지 않도록 조건문 use

방문 위치를 표시하기 위해 Array 만듦 -> 각 방문에 대한 표시를 노드 깊이로 설정 
"""


from collections import deque

def bfs(v):
    q=deque([v]) # 처음 들어오는 수빈이 위치 deque로 입력받기

    while q:
        v=q.popleft() # deque[0]값 찾기

        if v==k: # 값을 찾으면
            return visited[v] # 출력 
        
        for i in (v-1, v+1, 2*v):
            if not visited[i] and 0 <= i <= 100000:
                visited[i] = visited[v] + 1
                q.append(i)

n, k = map(int, input().split())
visited = [0 for i in range(100001)]

print(bfs(n))