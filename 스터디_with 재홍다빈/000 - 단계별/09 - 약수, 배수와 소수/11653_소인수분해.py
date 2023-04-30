n=int(input())

# 약수 구하기
"""
i=1
while (n !=1):
    if n%i==0:
        print(i)
    i+=1
"""
    

i = 2
while (n != 1):
    if n%i == 0:
        print(i)
        n /= i

    else:
        i+=1
