import sys

def is_balanced(p):
    l_count = 0
    r_count = 0
    for value in range(len(p)):
        if p[value] == '(':
            l_count += 1
        if p[value] == ')':
            r_count += 1
        if l_count == r_count:
            return value 
    return -1
        
def is_correct(p):
    stack = []
    for value in p:
        if not stack:
            stack.append(value)
        else:
            last = stack.pop()
            if last == '(' and value == ')':
                continue
            else:
                stack.append(last)
                stack.append(value)
    if stack :
        return False
    else : # stack이 비면 올바른 문자열 
        return True

def solution(p):
    answer = ''
    
    sys.setrecursionlimit(10**7)
    if is_correct(p):
        return p
    if not p:
        return ''
    
    index = is_balanced(p)
    
    u = p[: index + 1]
    v = p[index + 1:]

    if is_correct(u): # 올바른 문자열인 경우 v부터 시작 
        return u + solution(v)
    else: # 올바른 문자열이 아닌 경우 
        new_v = solution(v)
        new = '(' + new_v + ')'
        new_u = ''
        for value in range(1, len(u) - 1):
            if u[value] == '(':
                new_u += ')'
            else:
                new_u += '('
        new = new + new_u
        return new