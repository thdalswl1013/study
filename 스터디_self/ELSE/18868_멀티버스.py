m, n = map(int, input().split())

universe = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

for planet in range(m):
    for i in range(m):
        arr_sort = sorted(universe[i])  # 정렬 먼저 해준 후
        idx = []
        for j in universe[i]:  # 크기 순으로 인덱스 순서 리스트 만들기
            idx.append(arr_sort.index(j) + 1)
        universe[i] = idx

for i in range(m - 1):
    for j in range(i + 1, m):
        if universe[i] == universe[j]:  # 우주끼리 리스트 순서가 같으면 cnt++
            cnt += 1

print(cnt)