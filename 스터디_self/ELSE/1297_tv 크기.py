import math

# 대각선 길이 52 # 높이 비율 9 # 너비 비율 16
d, h, w = map(int,input().split())

re=math.sqrt(d**2 / (h**2 + w**2))
print(int(re*h), int(re*w))
