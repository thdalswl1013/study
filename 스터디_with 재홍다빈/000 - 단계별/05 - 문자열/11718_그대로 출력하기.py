while(1):
    try:
        print(input())
    except EOFError: # 입력의 끝을 알려주는 정보가 없으므로 try except 구문을 이용하여 EOFerror 예외 처리 해주기
        break