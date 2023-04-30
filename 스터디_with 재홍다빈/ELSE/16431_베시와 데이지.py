b1,b2=map(int, input().split()) # 베시: (3, 5) 출발
d1,d2=map(int, input().split()) # 데이지: (1, 1) 출발
j1,j2=map(int, input().split()) # 존: (2, 3) 서있음

bessie = max(abs(j1-b1), abs(j2-b2))
daisy = abs(j1-d1) + abs(j2-d2)

if bessie==daisy:
    print("tie")

elif bessie<daisy:
    print("bessie")

elif bessie>daisy:
    print("daisy")