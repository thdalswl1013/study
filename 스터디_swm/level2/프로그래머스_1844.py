from collections import deque

def move(x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

def solution(maps):
    answer = -1
    
    row = len(maps)
    col = len(maps[0])

    visited = [[False] * col for _ in range(row)]
    visited[0][0] = 1

    queue = deque([(0, 0)]) 
    
    while queue: # 큐가 빌 때까지
        x, y = queue.popleft() # 큐에서 원소를 꺼내서 목적지인지 아닌지 검사
        
        if x == row-1 and y == col-1: # 목적지라면 그때의 visited를 기록
            answer = visited[x][y]
            break
        
        for adj_x, adj_y in move(x, y): # 목적지가 아니라면 인접한 노드로 탐색을 이어감

            if 0 <= adj_x < row and 0 <= adj_y < col: # 지도의 범위를 벗어나지 않는 선에서
                if visited[adj_x][adj_y] == False and maps[adj_x][adj_y] == 1: # 인접 노드 조건: visited가 False이며, 벽이 아니여야함(=map이 1이어야 함)
                    queue.append((adj_x, adj_y)) # 인접노드라면 좌표를 큐에 넣고
                    visited[adj_x][adj_y] = visited[x][y] + 1 # 이전 노드의 visited값 +1로 갱신

    return answer