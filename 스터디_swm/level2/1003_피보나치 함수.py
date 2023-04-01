t = int(input())

def fibonacci(n):
    zero= [1, 0] # 0이 출력되는 횟수 
    one = [0, 1] # 1이 출력되는 횟수 

    if n > 1:
        for i in range(len(zero), n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

    print(zero[n], one[n])

for _ in range(t):
    n = int(input())
    fibonacci(n)