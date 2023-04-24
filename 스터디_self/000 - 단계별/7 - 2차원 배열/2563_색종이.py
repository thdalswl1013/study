# 도화지 크기만큼 반복문 돌아서 넓이가 존재한다면 그 넓이를 1로 바꿀 것 

n = int(input())
paper = [[0]*101 for i in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

cnt = 0
for i in paper:
    cnt +=sum(i)
print(cnt)