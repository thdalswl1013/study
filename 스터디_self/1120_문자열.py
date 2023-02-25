a, b = map(str, input().split())  # adaabc aababbc

result=[]
for i in range(len(b) - len(a) + 1): # 두 문자열 길이의 차이만큼 반복
    cnt=0

    for j in range(len(a)): # 반복문을 통해 b의 인덱스를 +i 해주면서 a의 문자열과 비교
        if a[j] != b[i+j]: # 다른 문자열이면 카운트
            cnt+=1

    result.append(cnt) # [3, 2]

print(min(result))
