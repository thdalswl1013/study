import itertools

n=int(input())
arr=list(map(int,input().split()))
nPr = list(itertools.permutations(arr, n)) 

# 제일 마지막 배열이면 뒤에 오는 배열이 없으므로 -1 출력
arr_reverse=[]
for i in range(n):
    arr_reverse.append(n-i)

if (arr==arr_reverse):
    print(-1)


# 그게 아니라면 순열 찾기

for i in range(len(list(nPr))):
    #print(arr)
    #print(list(nPr[i]))
    
    if (arr==list(nPr[i])):
        result=list(nPr[i+1])

for i in range(len(result)):
    print(result[i],end=' ')