n=int(input())
# f(A) = A의 약수의 합
# g(N) = f(1) + f(2) + ... + f(N)

sum=0
for i in range(1, n+1):
    sum += i * (n//i) # g(n) = (1 * n/1) + (2 * n/2) + .. + (n * n/n)

print(sum)