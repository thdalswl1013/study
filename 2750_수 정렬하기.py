n=int(input())
n_sort=[]

for i in range(n):
    n_sort.append(int(input()))

n_sort=sorted(n_sort)

for i in range(len(n_sort)):
    print(n_sort[i])
