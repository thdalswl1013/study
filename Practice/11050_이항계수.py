N, K = map(int, input().split())

def factorial(n):
    if n>1:
        return n*factorial(n-1)

    else:
        return 1

print(int(factorial(N)/(factorial(K)*factorial(N-K))))
