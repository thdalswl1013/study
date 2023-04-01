"""
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
"""


x=int(input()) # 몇 번의 case를 반복할 건지

for i in range(x):
    # n: 문서의 개수(list 길이)
    # m: 몇 번째 수가 몇 번째에 큐를 빠져나오는지 
    n, m= map(int, input().split())
    queue= list(map(int, input().split()))
    
    count=0 # m이 queue를 몇 번째에 빠져나갔는지 저장장

    while(m!=-1): # m==-1이면 종료
        if queue[0]==max(queue): # 큐의 맨 앞이 가장 크면
            del queue[0] # 삭제
            m-=1 # m이 한 칸 앞을 가리키게 함
            count+=1
        
        else: # 큐의 맨 앞이 가장 큰 게 아니라면
            queue.append(queue[0]) # 추가
            del queue[0] # 맨 앞 삭제

            if m==0: 
                m=len(queue)-1

            else: 
                m-=1
                
    print(count)
            
    