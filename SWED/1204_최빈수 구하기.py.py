t = int(input())

for j in range(t) :
    tc = int(input())
    score = list(map(int, input().split()))
    data = [0] * 1001

    for i in score :
        data[i] += 1 

    max_value = max(data)    
    result = []

    for i in range(len(data)) :
        if data[i] == max_value :
            result.append(i)

    print(result)
    print('#%d %d' % (tc, max(result)))