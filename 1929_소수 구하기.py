M,N=map(int, input().split()) # 3, 16

list_result=[]

for i in range(M,N+1): # 3~16 범위 뒤지기
    
    if i==1: 
        continue

    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            break
    
    else:
        print(i)
