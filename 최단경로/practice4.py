# 1번부터 각각 최단 거리를 구해서 가장 먼 최단 거리를 가진 곳을 구하면 되므로 다익스트라 사용
# 모든 노드 사이의 최단 거리를 구할 필요가 없기 때문에 

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)] # 1번부터 n + 1까지이므로 

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append((b, 1)) # 통로 하나당 1
        graph[b].append((a, 1)) # 양방향이므로 
    
    distance = [INF] * (n + 1)

    q = []
    distance[1] = 0 # 1번부터 시작하므로 
    heapq.heappush(q, (0, 1)) 

    while q:
        dis, node = heapq.heappop(q)
        if distance[node] < dis: # 이미 탐색했으므로 
            continue
        
        for i in graph[node]:
            cost = dis + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
    max_value = -1 # 헛간 최단 거리 중 최댓값 
    for i in range(2, n + 1):
        if max_value < distance[i] and distance[i] < INF: # 갈 수 있는 곳 중 최댓값 
            max_value = distance[i]

    print(distance.index(max_value), max_value, distance.count(max_value))
        

if __name__ ==  "__main__":
    main()