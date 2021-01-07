# 가장 큰 수를 만들 수 있는 규칙은 앞에서부터 수들을 탐색하여 만약 탐색했던 수 보다 큰 수가 나올 경우 이전에 탐색된 수들을 제거하는 것.
# 탐색한 애들을 stack에 넣어서 굳이 여러번 number를 탐색하지 않아도 될 수 있도록 진행한다
# 그래야 시간 초과가 안난다. 이전에 탐색한 숫자가 현재 탐색한 숫자보다 작으면 제거 
def solution(number, k):
    answer = ''
    
    stack = []
    remain_count = len(number) - k
    
    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
            continue
        is_done = False
        while stack and stack[-1] < number[i]:
            stack.pop(-1)
            k -= 1
            if k == 0:
                stack += number[i:]
                is_done = True
                break
        if is_done:
            break
        stack.append(number[i])     
                
    if len(stack) > remain_count:
        stack =  number[:remain_count]
        
    answer = "".join(stack)
    return answer