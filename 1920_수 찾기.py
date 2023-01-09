N=int(input())
A=list(map(int, input().split(' ')))
A.sort()

M=int(input())
num=list(map(int, input().split(' ')))


def find(num):
    left = 0
    right = N-1

    while left<=right:
        mid = (left + right) // 2

        if A[mid] == num:
            return True

        if A[mid] < num:
            left = mid + 1    

        if A[mid] > num:
            right = mid - 1   


for i in range(M):
    if find(num[i]):
        print(1)
    else:
        print(0)        

