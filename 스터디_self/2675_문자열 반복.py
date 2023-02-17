t=int(input())

for i in range(t):
    num, string=input().split()
    
    text=''

    for j in string:
        text+=int(num)*j

    print(text)
