from collections import deque

def dfs(index, t_score, t_cal):
    global max_value

    if t_cal > l:
        return 
    
    if index >= n:
        if t_score > max_value:
            max_value = t_score
    
        return 
    
    dfs(index + 1, t_score + hamburgers[index][0], t_cal + hamburgers[index][1]) # 해당 햄버거를 더하거나 
    dfs(index + 1, t_score, t_cal) # 해당 햄버거를 더하지 않거나 
     

T = int(input())
for t in range(T):
    n, l = map(int, input().split())
    
    hamburgers = []
    for i in range(n):
        a, b = map(int, input().split())
        hamburgers.append((a, b, [i]))
    
    max_value = 0
    
    dfs(0, 0, 0)

    print("#" + str(t + 1), max_value)