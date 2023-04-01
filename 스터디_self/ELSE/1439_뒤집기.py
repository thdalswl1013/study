s=list(input()) # ['0', '0', '0', '1', '1', '0', '0']

cnt=0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt+=1

print((cnt+1)//2)
