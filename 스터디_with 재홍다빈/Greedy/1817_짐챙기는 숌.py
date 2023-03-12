"""
if) 짐의 개수가 0개인 경우 0을 출력

else) 
   책이 차곡차곡 쌓여 있기 때문에 반복문을 역방향으로 수행
   확인중인 책을 현재 박스에 담아 그 무게를 박스에 더함
   책을 더했을 때의 박스 무게가 입력받은 m보다 더 크면, 박스를 하나 추가하고, 그 박스에 방금의 책을 담음.

   그 박스에 다시 새로운 책들을 추가해주고, 그렇게 반복문이 종료될 때까지 반복
"""

n, m =map(int,input().split()) # 책 6권, 최대 무게 10kg

if n==0:
    print(0)

elif n!=0:
    bag=list(map(int,input().split())) # 5 5 5 5 5 5 

    result=1
    weight=0
    for i in range(n-1, -1, -1):
        weight+=bag[i]

        if weight>m:
            result+=1
            weight=bag[i]
    print(result)
    

