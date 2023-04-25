x,y,w,h=map(int,input().split())

"""
한수 위치: (6,2)
직사각형 : (0,0) ~ (10,3)
"""

print(min(abs(x-w), abs(y-h), x, y))