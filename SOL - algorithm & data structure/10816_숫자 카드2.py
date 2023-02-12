from selectors import EpollSelector
import sys

n_mine=int(sys.stdin.readline()) # 10
card_mine=list(map(int, sys.stdin.readline().split(' '))) # 6 3 2 10 10 10 -10 -10 7 3

n_yours=int(sys.stdin.readline()) # 8
card_yours=list(map(int, sys.stdin.readline().split(' ')))

def binarySearch(array, target, left, right):
    middle=(left+right)//2

    if array[middle] > target:
        right=middle - 1

    elif array[middle] < target:
        left=middle + 1

    elif array[middle]==target:
        return middle

