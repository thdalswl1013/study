word = list(map(str, input().rstrip("\n"))) # ['m', 'o', 'b', 'i', 't', 'e', 'l']
result=[]

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        firstWord=word[:i]
        secondWord=word[i:j]
        thirdWord=word[j:]

        firstWord.reverse()
        secondWord.reverse()
        thirdWord.reverse()

        result.append("".join(firstWord+secondWord+thirdWord))

print(min(result))