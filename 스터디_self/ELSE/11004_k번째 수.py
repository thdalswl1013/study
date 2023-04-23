n, k = map(int, input().split())
a=list(map(int, input().split())) # 4 1 2 3 5
a.sort()

print(a[k-1])