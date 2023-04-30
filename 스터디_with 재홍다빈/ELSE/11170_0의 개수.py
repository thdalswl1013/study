n=int(input())

for i in range(n):
    x, y = map(int, input().split())
    count=0

    for j in range(x, y+1):
        w = str(j)

        count+=w.count('0')

    print(count)