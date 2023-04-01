baekjoon = list((input()))
alphabet="abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    if i in baekjoon:
        print(baekjoon.index(i), end= ' ') # 1 0 2 4 3 7 5
    
    else:
        print(-1, end =' ')