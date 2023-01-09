# 재귀함수와 백트래킹을 활용한 풀이법 

n, s = map(int, input().split()) # 5 0
arr=list(map(int, input().split())) # -7 -3 -2 4 8

count=0

def dfs(index, subsetSum):
    global count # 전역변수의 데이터를 확인할 수는 있지만 수정할 수 없으므로 global로 정의해야 수정 가능함

    if index>=n:
        return
    
    # 지금까지 구해온 subsetSum에 0~(n-1) 인덱스 원소 값을 더하는 경우, 더하지 않는 경우로 나눠서 재귀함수 호출

    subsetSum+=arr[index] 

    if subsetSum==s: # subsetSum이 구하려는 값(s)와 같다면 전역변수 count에 +1 -> 개수 확인
        count+=1
    
    dfs(index+1, subsetSum) # 현재 arr[index]를 선택한 경우
    dfs(index+1, subsetSum - arr[index]) # 현재 arr[index]를 선택하지 않은 경우

dfs(0, 0)
print(count)
