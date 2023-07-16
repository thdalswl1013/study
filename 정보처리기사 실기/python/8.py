# 다음 Python 코드는 "30, 200"을 출력한다. 빈 칸 ( 1 ), ( 2 )에 알맞는 코드를 차례로 쓰시오.

class Calculator:
    def add(self,x,y):
        return x + y
    def mul(self,x,y):
        return x * y
 
cal = Calculator()
x = cal.add(10,20)
y = cal.mul(10,20)
 
print(x, y)
 