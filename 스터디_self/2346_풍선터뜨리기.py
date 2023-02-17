import sys
from collections import deque

n=int(input())
q = deque(enumerate(map(int, input().split())))
"""
enumerate 사용 전: deque([3, 2, 1, -3, -1])
enumerate 사용 후: deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])
"""
ans = []

while q:
    idx, paper = q.popleft() #idx에는 0, paper에는 3이 처음에 저장됨
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
        
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, ans)))