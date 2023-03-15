"""
- 반복문을 통해 줄의 번호와 프렛의 번호를 입력받아 확인한다.
- 주어진 줄의 더 높은 프렛을 누르고 있는 경우에 while문을 통해 손가락을 하나씩 뗀다.
- 이미 누르고 있는 줄의 프렛인 경우 패스한다.
- 주어진 줄의 프렛이 누르고 있는 프렛보다 높고 같지 않은 경우 프렛을 누른다.
"""

N, P = map(int, input().split())
line = [[0] for i in range(7)]

cnt = 0

# 반복문을 통해 줄의 번호와 프렛의 번호를 확인
for i in range(N):
    line_num, plat_num = map(int,input().split())

    while line[line_num][-1] > plat_num: # 주어진 줄의 더 높은 프렛을 누르고 있는 경우, 손가락을 하나씩 뗀다.
        line[line_num].pop()
        cnt += 1

    if line[line_num][-1] == plat_num: # 이미 누르고 있는 줄의 프렛인 경우 패스
        continue

    line[line_num].append(plat_num) # 주어진 줄의 프렛을 누른다.
    cnt += 1

print(cnt)
