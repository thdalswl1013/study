a = [[1,1,0,1,0],
     [1,0,1,0]]
tot,totsu = 0, 0
for i in a:
    for j in i:
        tot += j # tot=5
    totsu = totsu + len(i) # totsu=9
print(totsu, tot)