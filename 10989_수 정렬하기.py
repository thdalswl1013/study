import sys
input=sys.stdin.readline 
n=int(input())

n_sort=[0]*10000


for i in range(n):
#반복문 안에서 입력받을 때는 시간초과를 고려하여 input 대신 sys.stdin.readline 이용
    n_sort[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    if n_sort[i] !=0:
        for j in range(n_sort[i]):
            print(i+1)