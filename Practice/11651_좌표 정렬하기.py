# y 좌표를 오름차순으로 정렬

import sys

n=int(sys.stdin.readline())
point=[]

for i in range(n):
    [a,b] = map(int, input().split())

    point.append([a,b])

sorted_point=sorted(point)

for i in range(n):
    print(sorted_point[i][0], sorted_point[i][1])
