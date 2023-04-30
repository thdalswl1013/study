n=int(input())

def factorial(n):
    if n > 1:
        return factorial(n-1)*n
    elif n == 1:
        return 1

list_n=list(str(factorial(n)))
cnt=0

while(list_n[-1]=="0"):
    cnt+=1
    list_n.pop()

print(cnt)