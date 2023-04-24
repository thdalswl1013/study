n = int(input())

# 초기값
a=[4] # 초기 상태
f = 2 # 초기 상태 한 변에 있는 점의개수
x = 1

for i in range(15):
    f += x
    a.append(f*f)
    x *= 2

print(a[n])