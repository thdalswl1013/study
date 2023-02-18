
computer = int(input()) # 컴퓨터의 수
pair = int(input()) # 네트워크 상에서 직접 연결되어있는 컴퓨터 쌍의 수

arr=[]

for i in range(pair):
    x, y= map(int, input().split())
    arr.append([x,y])

print(arr) # [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]