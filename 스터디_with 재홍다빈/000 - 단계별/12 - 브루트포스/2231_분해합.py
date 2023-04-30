n = int(input()) 

for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
    arr = list((map(int, str(i))))  # i의 각 자릿수를 리스트로 만듦
    num_sum = i + sum(arr)  # 분해합 = 생성자 + 각 자릿수의 합

    if num_sum == n: # 처음으로 분해합과 입력값이 같을때 가장 작은 생성자
        print(i)
        break
    if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)