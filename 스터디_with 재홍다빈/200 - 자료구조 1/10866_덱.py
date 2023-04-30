from collections import deque # 덱 = 양방향 큐 
import sys

d = deque() # 튜플
n = int(input())

for i in range(n):
    sen = sys.stdin.readline().split()
    # print(sen)

    if sen[0] == "push_front": # 정수를 덱의 앞에 넣는다. -> appendleft() 함수를 이용.
        d.appendleft(sen[1])


    elif sen[0] == "push_back": # 정수를 덱의 뒤에 넣는다. 
        d.append(sen[1])


    elif sen[0] == "pop_front": # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. -> popleft() 함수를 이용.
                                # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if d:
            print(d[0])
            d.popleft()

        else:
            print(-1)


    elif sen[0] == "pop_back": # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.
                               # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if d:
            print(d[len(d) - 1])    
            d.pop()
        else:
            print(-1)


    elif sen[0] == "size": # 덱에 들어있는 정수의 개수를 출력한다.
        print(len(d))


    elif sen[0] == "empty": # 덱이 비어있으면 1을, 아니면 0을 출력한다.
        if d:
            print(0)
        else:
            print(1)


    elif sen[0] == "front": # 덱의 가장 앞에 있는 정수를 출력한다.
                            # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

        if d: 
            print(d[0])
        else:
            print(-1)


    elif sen[0] == "back": # 덱의 가장 뒤에 있는 정수를 출력한다. 
                           # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.        
        if d:
            print(d[len(d) - 1])
        else:
            print("-1")
