import sys

n=int(sys.stdin.readline())
word=[]

for i in range(n):
    word.append(sys.stdin.readline().strip()) # strip이 문자열 맨 앞과 맨 끝의 공백문자를 제거해줌
# print(word) -> ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']

set_word=set(word)  # 집합과 관련된 것을 쉽게 처리하기 위해 만든 자료형 set 이용
                    # {'im', 'it', 'i', 'no', 'wont', 'hesitate', 'but', 'more', 'cannot', 'yours', 'wait'}
word=list(set_word) # ['im', 'it', 'i', 'no', 'wont', 'hesitate', 'but', 'more', 'cannot', 'yours', 'wait']
word.sort() # 중복 제거
word.sort(key=len)  # 길이 순으로 sort
                    # ['i', 'im', 'it', 'no', 'but', 'wait', 'wont', 'more', 'yours', 'cannot', 'hesitate']

for i in word:
    print(i)