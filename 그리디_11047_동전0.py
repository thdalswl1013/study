"""
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
   -> [i ≥ 2인 경우에 Ai는 Ai-1의 배수] = [500원은 100원의 배수, 1000원은 500원의 배수, 10000원은 1000원의 배수,...]
   -> 그리디 사용 가능
"""


n, k= map(int, input().split())
coin=[]

for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

print(coin)

cnt=0
for i in range(n):
    if k==0:
        break
    else:
        cnt = cnt + k//coin[i]
        k = k % coin[i]
print(cnt)


"""
N, K = map(int, input().split())

nlist = []
for _ in range(N):
    nlist.append(int(input()))
    
index = 0
count = 0

for _ in range(N-1):

    if nlist[index] < K:
        index = index+1

    elif nlist[index] > K:
        index -= 1
        break
    
for _ in range(N):
    
    c = K // nlist[index]
    count += c
    K -= c * nlist[index]
    index -= 1
    
    if K == 0:
        break

print(count)
"""