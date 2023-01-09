import sys

n=int(sys.stdin.readline())

num=list(map(int, sys.stdin.readline().split()))
num_set=list(set(num))

num_sort=sorted(num_set)

for i in num_sort:
    print(i, end=' ')
