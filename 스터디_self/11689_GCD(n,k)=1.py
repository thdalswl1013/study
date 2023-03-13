
# GCD(a,b)==1이라는 것은 a와 b가 서로소라는 뜻
# 서로소 구하는 공식: n * (1 - (1 / 소인수)) * (1 - (1 / 소인수)) ...

n=int(input())
result=n

for i in range(2, int(n**0.5)+1):
    if n%i==0:
        while n%i==0:
            n//=i
        result*=((i-1)/i)
    
if n>1:
    result*=1-(1/n)

print(int(result))