t=int(input())

for x in range(t):
    n=int(input()) # 13
    n_binary=bin(n)[2:] # 1101

    for i in range(len(n_binary)):
        
        if n_binary[-i-1] == '1':
            print(i, end=' ')