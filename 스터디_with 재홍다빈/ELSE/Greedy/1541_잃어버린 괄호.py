"""
양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 괄호를 모두 지웠다.
괄호를 적절히 쳐서 이 식의 값을 "최소"로 만들려고 한다. -> '-' 에서 가장 많이 빼면 됨 
"""

array=input().split('-') # ['55', '50+40']

result=0

for i in array[0].split('+'):
    result += int(i) # result = 55


for i in array[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)


"""
array=input().split('-') # ['55', '50+40']

result1=0

for i in equation[0].split('+'):
    result1+=int(i)

result2=0

if len(equation)==2:
    for i in equation[1].split('+'):
        result2+=int(i)

print(result1 - result2)
"""