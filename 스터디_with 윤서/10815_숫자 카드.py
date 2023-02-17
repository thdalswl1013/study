get_card=int(input()) # 5
get_card_arr=list(map(int, input().split(' '))) # 6 3 2 10 -10
get_card_arr.sort()

new_card=int(input()) # 8
new_card_arr=list(map(int, input().split(' '))) # 10 9 -5 2 3 4 5 -10

def binary_search(arr, target, left, right):
    while left<=right:

        mid=(left+right)//2

        if arr[mid]==target:
            return mid

        elif arr[mid]>target:
            right=mid-1

        elif arr[mid]<target:
            left=mid+1


for i in range(new_card):
        if binary_search(get_card_arr, new_card_arr[i], 0, get_card-1) is not None: # if A랑 if A is not none은 유사하지만 후자를 쓰는 것을 추천
            print(1, end=' ')                                                       # 이 문제에서는 후자로 쓰지 않아서 틀렸음
        else:
            print(0, end=' ')
