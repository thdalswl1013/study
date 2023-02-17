def dfs(depth, index):
    if depth==6:
        print(*result)
        return 

    for i in range(index, first):
        result.append(arraylist[i])
        dfs(depth+1, i+1)
        result.pop()
    
while True:
    arr=list(map(int,input().split())) # 7 1 2 3 4 5 6 7 
    #print(arr)

    first=arr[0] # 7
    arraylist=arr[1:] # 1 2 3 4 5 6 7
    result=[]

    dfs(0,0)

    if first==0:
        exit()
    print()
