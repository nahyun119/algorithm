import heapq
INF = 1e9

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for e in edge:
        a, b = e[0], e[1]
        graph[a].append(b)
        graph[b].append(a)
    
    q = []
    distance[1] = 0 # 1번 노드 
    heapq.heappush(q, (0, 1))
    
    while q:
        dis, node = heapq.heappop(q)
        if distance[node] < dis: # 이미 최단경로인 경우 
            continue
        
        for i in graph[node]:
            cost = distance[node] + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
                
    max_value = max(distance[1:])
    answer = distance.count(max_value)
    
    
    return answer