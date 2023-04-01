
baekjoon=list(map(str, input())) # ['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n']
temp=[0] * len(baekjoon)

for i in range(len(baekjoon)):
    temp[i]="".join(baekjoon)
    del(baekjoon[0])

temp.sort()

for i in range(len(temp)):
    print(temp[i])