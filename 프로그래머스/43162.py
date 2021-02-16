# 처음엔 dfs로 풀어볼까했는데 computers 보고
# 근데 그냥 연결된거니까 bfs로 생각해도 될 것 같다. 

from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    count = 0
    
    for i in range(n):
        q = deque()
        q.append(i)
        #print(i, visited)
        if visited[i] == 1: # 이미 방문한 경우 continue
            continue
        if 0 not in visited: # 모든 컴퓨터에 방문한 경우 종료 
            break 
            
        visited[i] = 1
        
        while q:
            node = q.popleft()
            
            for j in range(n):
                if computers[node][j] == 1 and j != node and visited[j] == 0:
                    q.append(j)
                    visited[j] = 1
        count += 1
    
    answer = count
    return answer