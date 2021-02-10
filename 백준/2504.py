import sys

input = sys.stdin.readline

def main():
    string = input().strip()

    st_list = list(string)
    print(st_list)

    small_p = ['(', ')']
    large_p = ['[', ']']

    length = len(st_list)

    stack = []
    operator = []
    answer = 0
    score = 0          

    for value in st_list:
        if not stack:
            stack.append(value)
        else:
            p = stack[-1]
            stack.append(value)
            if p in small_p and value in small_p:
                if p != value:
                    stack.pop()
                    stack.pop()
                    operator.append(2)
                    operator.append('+')
                else:
                    operator.append(2)
                    operator.append('*')
                    operator.append('(')
                

    for index, value in enumerate(st_list):
        print(stack, score, answer)
        if not stack: # 괄호가 다시 시작하거나, 맨 처음인 경우 
            answer += score 
            stack.append((index, value))
            score = 0 # 괄호 점수 초기화 
        else:
            p = stack[-1]
            stack.append((index, value))
            if value in small_p and p in small_p: # stack 안에 결과랑 value가 모두 소괄호인 경우    
                if value != p[1]: # 괄호가 맞다
                    stack.pop()
                    stack.pop()
                    # if score == 0: # 괄호 안에 괄호가 없는 경우
                    #     score += 2
                    # else: # 괄호가 있는 경우
                    #     score += score * 2
                else: # 같은 괄호인 경우 
                    operator.append(2) # 곱하기 
            elif value in large_p and p in large_p: # stack 안에 결과랑 value가 모두 대괄호인 경우 
                if value != p[1]: # 괄호가 맞다
                    stack.pop()
                    stack.pop()
                    # if score == 0 : # 괄호 안에 괄호가 없는 경우
                    #     score += 3
                    # else:
                    #     score += score * 3
                else:
                    operator.append(1)
            else: # 두 개가 다른 괄호인 경우 ( ] 이런 식



    # 스택이 비지 않으면 올바른 괄호가 아님 
    if stack:
        print(0)
    else:
        print(answer)

if __name__ ==  "__main__":
    main()