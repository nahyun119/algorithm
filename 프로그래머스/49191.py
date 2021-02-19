INF = 1e9
def solution(n, results):
    answer = 0
    
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for result in results:
        a, b = result[0], result[1]
        graph[a][b] = 1
        #graph[b][a] = 1
        
    for i in range(1, n + 1):
        graph[i][i] = 0
    
    
    for i in range(1, n + 1): # 거쳐가는 노드가 반복문 제일 처음 
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
    #print(graph)
    result = 0
    for a in range(1, n + 1):
        count = 0
        for b in range(1, n + 1):
            if graph[a][b] != INF or graph[b][a] != INF: # 이어져있다는 의미
                count += 1
            if count == n:
                result += 1
    answer = result
            
    return answer