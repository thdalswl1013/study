import sys

list_left=list(sys.stdin.readline().rstrip()) #abcd
list_right=[]

n=int(sys.stdin.readline()) #3

for i in range(n):
    command=list(sys.stdin.readline().split()) 

    # 커서를 왼쪽으로 한 칸 옮김
    if command[0] == "L": 
        if list_left: #커서가 문장의 맨 앞이면 무시되므로, 맨 앞이 아닌 경우만
            list_right.append(list_left.pop())

    # 커서를 오른쪽으로 한 칸 옮김
    elif command[0] == "D":
        if list_right: #커서가 문장의 맨 뒤면 무시되므로, 맨 뒤가 아닌 경우만
            list_left.append(list_right.pop())

    # 커서 왼쪽에 있는 문자를 삭제함
    elif command[0] == "B": 
        if list_left: #커서가 문장의 맨 앞이면 무시되므로, 맨 앞이 아닌 경우만
            list_left.pop()

    # 문자를 커서 왼쪽에 추가함
    elif command[0] == "P":
        list_left.append(command[1])

#print(list_before) -> ['a', 'b', 'c', 'd', 'y']
#print(list_after)  -> ['x']
list_left.extend(list_right) #list_after를 list_before 뒤에 붙인다 -> ['a', 'b', 'c', 'd', 'y', 'x']

print(''.join(list_left)) #''.join(리스트): ['a', 'b', 'c']같은 이런 리스트를  abc같은 이런 문자열로 반환해주는 함수 
