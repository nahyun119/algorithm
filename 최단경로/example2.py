# 거쳐가는 것이 없고 시작점에서 다른 도시로 이동하는 경우를 확인하므로 다익스트라

import heapq 
import sys 

input = sys.stdin.readline # 범위가 크기때문에 
INF = int(1e9)

def main():
    n, m, c = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append((y, z)) # y노드로 z 거리 
    
    distance = [INF] * (n + 1)

    q = []
    distance[c] = 0
    heapq.heappush(q, (0, c)) # 시작점 정보를 우선순위 큐에 추가 

    while q:
        dis, node = heapq.heappop(q)

        if distance[node] < dis: # 이미 탐색한 노드이므로 
            continue

        for i in graph[node]: # 이어진 간선 탐색
            cost = distance[node] + i[1] # node까지 거리랑 이동거리 더해서 i[0] 까지 가는 비용 계산
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 우선순위 큐에 추가 

    max_value = -1
    count = 0

    for i in range(1, n + 1):
        if distance[i] < INF:
            count += 1 # c 에서 이동할 수 있는 도시 수 구하기
            if distance[i] > max_value:
                max_value = distance[i] # 최단 거리 중 제일 오래 걸리는 경로 구하기
    
    print(count - 1, max_value) # 자기 자신 제외해야하므로 count - 1
 

    #print(distance)
            

        



if __name__ ==  "__main__":
    main()