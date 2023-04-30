"""
362 10진수 -> 362=10*36+2
              나머지 2는 10진수에서 2번째 숫자임 -> 그 값을 정답에 추가
              몫인 36을 10으로 나누면 나머지 6 -> 그 값을 정답에 추가
              이런식으로 반복하면 정답이 263이 되고 그걸 뒤집어서 저장하면 진법 전환이 완료된 것
"""


n,b=map(int,input().split())

temp="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result=""

while n!=0:
    result+=str(temp[n%b])
    n//=b

print(result[::-1])