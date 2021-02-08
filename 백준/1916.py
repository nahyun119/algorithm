# a 도시에서 b 도시로 이동할 수 있는 최소 비용 -> 최단 경로 -> 다익스트라

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def main():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]


    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    
    start, end = map(int, input().split())

    distance = [INF] * (n + 1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dis, node = heapq.heappop(q)
        if distance[node] < dis: # 이미 최소를 기록함 방문해서 
            continue
        
        for i, cost in graph[node]:
            cost = cost + dis
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
        
    print(distance[end])


    
if __name__ ==  "__main__":
    main()