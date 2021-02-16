# 한 단어만 차이나는지를 확인을 하는 부분이 애매해서 오류가 났었다.
# 자세히 잘 살펴볼 것! 

from collections import deque

def check(n_list, s_list):
    count = 0
    for i in range(len(n_list)):
        if n_list[i] != s_list[i]:
            count += 1
    if count == 1:
        return True
    return False 
        
def solution(begin, target, words):

    length = len(words)
    
    visited = [0] * length 
    
    q = deque()
    q.append((begin, 0))

    #print(check(['h', 'i', 't'], ['h', 'i', 'h']))
    
    while q:
        node, n = q.popleft()
        n_list = list(node)
        
        for i in range(length):
            s_list = list(words[i])
            # temp = [x for x in n_list if x not in s_list]
            
            if check(n_list, s_list) and visited[i] == 0: # 하나만 차이나는 경우 
                if words[i] == target: #갈 수 있는 것중에 target이 있으면 바로 종료 
                    return n + 1
                q.append((words[i], n + 1))
                visited[i] = 1 
    return 0