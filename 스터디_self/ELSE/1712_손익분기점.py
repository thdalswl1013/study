
a, b, c = list(map(int, input().split())) # a: 고정 비용, b: 가변 비용, c: 노트북 가격

# break point: 고정비용 + 가변비용 < 판매수익 최초 지점

if b<c:
    print(int(a/(c-b))+1)

else:
    print(-1)