r= 1000000

check = [True for _ in range(r)]

for i in range(2,int(r**0.6)):
    if check[i]==True:
        for j in range(i*2, r, i) : 
            if check[j] == True :
                check[j] = False            #에라토스테네스의 체


import sys
input = sys.stdin.readline


while(True):                               #입력받은 수가 에라토스테네스의 체에 속하는지, 즉 소수인지
    n = int(input())

    if n==0 : break
    for i in range(3,r):
        if check[i] == True:
            if check[n-i] == True :
                print("%d = %d + %d"%(n , i , n-i))
                break