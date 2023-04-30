n=int(input())

for i in range(n):
    sentence=input().split()

    for j in range(len(sentence)):
        sentence_list=list(sentence[j])
        sentence_list.reverse()
        print(''.join(sentence_list), end=' ')