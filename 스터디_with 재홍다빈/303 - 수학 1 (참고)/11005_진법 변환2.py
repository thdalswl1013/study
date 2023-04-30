n, b = map(int, input().split())
original='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 그냥 문자 나열하는 게 효율적이었음 

def func(n, b): # n을 b진수로 변환 
    result=''

    while n: 
        result  += str(original[n%b]) 
        n //= b
    
    print(result[::-1]) # 답을 뒤집어서 출력 

func(n, b)

