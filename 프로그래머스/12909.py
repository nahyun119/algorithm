def solution(s):
    answer = True
    
    stack = []
    
    s_list = list(s)
    
    for p in s_list:
        if not stack:
            stack.append(p)
        else:
            s_p = stack[-1]
            if s_p == '(' and p == ')': # 다르다면 
                stack.pop()
            else: # 같다면
                stack.append(p)
                
    if stack: # 비지 않으면 False    
        return False
        
                

    return True