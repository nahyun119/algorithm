# 시작점이 1번이라서 1번부터 다른 노드까지 최단 경로를 구해서 
# 1번 -> k번으로 이동하는 최단 경로를 구하고
# k번부터 다른 노드까지 최단 경로를 구해서 
# k번 -> x번으로 이동하는 최단 경로를 구한다음
# 두 경로를 더하면 된다고 생각해서 다익스트라로 풀었다..
# 거쳐가는 경로의 최단 거리라서 플로이드일 것 같긴 했는데,,
# 전형적인 플로이드 문제다,, -> example1-1.py

import heapq

INF = int(1e9)

def dijkstra(start, graph, N):
    q = []
    distance = [INF] * (N + 1)

    distance[start] = 0 # 시작 위치는 0으로 설정
    heapq.heappush(q, (0, start)) # 시작하는거 q에 추가 

    while q:
        dis, node = heapq.heappop(q)
        
        if distance[node] < dis: # 이미 탐색한 노드이므로 
            continue
        for i in graph[node]:
            cost = distance[node] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))

    return distance


def main():
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
     
    for _ in range(M): # 그래프 입력 받기
        a, b = map(int, input().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1)) # 양방향이므로 
    
    X, K = map(int, input().split())

    result1 = dijkstra(1, graph, N) # 1에서의 모든 최단 경로를 구한다 
    result2 = dijkstra(K, graph, N) # k에서의 모든 최단 경로를 구한다

    dist1 = result1[K]
    dist2 = result2[X]

    if dist1 == INF or dist2 == INF:
        print(-1)
    else:
        print(dist1 + dist2)

    


if __name__ ==  "__main__":
    main()