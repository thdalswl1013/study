
yeondu=input()

n=int(input())
n_list=[]
for i in range(n):
    n_list.append(input())
n_list.sort()

result=[]
max=0
max_i=0
for i in range(n):
    L= n_list[i].count('L') + yeondu.count('L')
    O= n_list[i].count('O') + yeondu.count('O')
    V= n_list[i].count('V') + yeondu.count('V')
    E= n_list[i].count('E') + yeondu.count('E')

    expression = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    
    if expression > max:
        max = expression
        max_i = i

print(n_list[max_i])