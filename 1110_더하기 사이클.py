N=int(input())

def algorithm(start):
    if start>=10:
        start//10 + start%10 # 10의 자리 수 # 1의 자리 수
    
count=0
num=N

while True:
    a= num//10
    b= num%10
    c= (a+b)%10
    num=(10*b)+c

    count+=1

    if(num==N):
        break
print(count)