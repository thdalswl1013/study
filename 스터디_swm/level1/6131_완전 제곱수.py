n=int(input())

#a*a  - b*b = n

cnt=0
for i in range(1, 501):
    for j in range(1, 501):
        if i*i - j*j==n:
            cnt+=1
print(cnt)