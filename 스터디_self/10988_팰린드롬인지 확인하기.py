voca=input()
voca_reverse=[]

for i in voca:
    voca_reverse.append(i)
voca_reverse.reverse()
voca_reverse="".join(voca_reverse)

if voca==voca_reverse:
    print(1)
else:
    print(0)