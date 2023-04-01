def solution(numbers, target):
    answer = 0 # 타겟 넘버를 만드는 방법의 수(구하려는 애)
    check = [0] # 타겟과 비교할 수를 넣을 배열
    
    for i in numbers:
        temp = [] # 한 사이클 결과값 임시 저장 배열
        for j in check:
            temp.append(j + i)
            temp.append(j - i)
        check = temp # 임시 저장 배열 res에 넣어주기
    
    for i in check:
        if i == target: # 타겟과 res[i]값 비교
            answer += 1
    
    return answer