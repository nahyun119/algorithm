# 어찌저찌 풀긴했는데,,, 될거라고 생각을 안해서 왜 되는거지라는 의문을 아직 품고있다,, 오류때문에 좀 고생했는데,, 쉽게해결해서,,

import itertools
import copy

def solution(expression):
    answer = 0
    
    op = ['*', '+', '-']
    operators = list(itertools.permutations(op ,3)) # 먼저 가능한 우선순위 목록을 고른다. 
    
    expressions = []
    num = ''
    for e in expression: # 그리고 문자열인 expression을 숫자랑 연산자랑 분리하여 배열에 저장한다. 
        if e != '*' and e != '-' and e != '+':
            num += e
        else:
            expressions.append(int(num))
            expressions.append(e)
            num = ''
    expressions.append(int(num))
    
    max_value = 0
    
    for operator in operators: # 가능한 우선순위 별로 확인 
        e = copy.deepcopy(expressions) # 여러번 이용하므로 deepcopy를 해서 사용한다. 
        
        for o in operator: # 우선순위 별로 연산 시작 
            
            while True:
                if o not in e: # 연산자가 없으면 종료 
                    break 
                else: # 연산자가 있으면 연산자 위치를 찾고 숫자들을 가져온다. 
                    i = e.index(o)
                    num1 = e[i - 1]
                    num2 = e[i + 1]
                    if o == '*':
                        value = num1 * num2
                    if o == '+':
                        value = num1 + num2
                    if o == '-':
                        value = num1 - num2
                    # 이 때 새롭게 식을 업데이트 해야하는데, 연산자랑 숫자들은 제외해야하므로 이 인덱스들을 빼고 리스트를 새로 만든다. -> 이 부분을 되게 애먹음 
                    # pop이나 이런거 쓰면 인덱스도 안맞고 계속 시시각각 바뀌니까 ㅠ 
                    e = [x for ind, x in enumerate(e) if ind != i and ind != i - 1 and ind != i +1]
                    e.insert(i - 1, value) # -> 그리고 연산한 값을 연산자 있던 곳 앞으로 넣는다. 
                    
        if abs(e[0]) > max_value: # 마지막으로 절댓값이랑 최댓값 비교해서 
            max_value = abs(e[0])
    
    print(max_value)
    answer = max_value
    return answer
