
"""
3이라는 수가 주어지면 3의 배수중에 1로만 이루어진 수 중 가장 작은 수를 찾으면 된다
->  3의 배수 중 1로만 이루어진 가장 작은 수는 111이라서, 정답은 111의 자릿수인 3이다.
"""


while True:
    try:
        n = int(input())
    except:
        break

    num = 0; i = 1
    
    while True:
        num = (num*10) + 1 # 1부터 시작해서 10을 곱하고, 1을 더해서
        num %= n # 그 수가 입력받은 수로 나눠질 수 있는지 확인

        if num == 0:
            print(i)
            break

        i+=1
