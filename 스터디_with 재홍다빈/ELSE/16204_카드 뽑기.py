n, m, k = map(int, input().split())

# 4개의 카드 중 3개의 카드 앞면에 o 한 개, 나머지 1개의 카드 앞면에는 x 한 개

print(min(m, k) + n - max(m, k))