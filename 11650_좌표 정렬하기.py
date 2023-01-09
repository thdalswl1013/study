# x 좌표를 오름차순으로 정렬

import sys

n=int(sys.stdin.readline())
point=[]

for i in range(n):
    """
    point=sys.stdin.readline().split()
    x=point[0]
    y=point[1]   
    """
    [x,y] = map(int, input().split()) # map은 리스트의 요소를 지정된 함수로 처리해주는 함수

    point.append([y,x])

sorted_point=sorted(point) 

for i in range(n):
    print(sorted_point[i][1], sorted_point[i][0])
