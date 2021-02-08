# 다익스트라 최단경로 알고리즘
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def main():
    v, e = map(int, input().split())
    k = int(input())

    distance = [INF] * (v + 1)
    graph = [[] for _ in range(v + 1)]


    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    q = []
    distance[k] = 0 # 자기 자신이므로 
    heapq.heappush(q, (0, k))
    
    while q:
        cost, end = heapq.heappop(q)
        if distance[end] < cost: # 이미 탐색했으므로 (최솟값이 이미 정해짐)
            continue
        for i in graph[end]:
            dis = cost + i[1] # end를 거쳐서 i까지 가는 비용 계산 
            if dis < distance[i[0]]: # i까지 가는 거리랑 end 거쳐서 가는 비용이랑 비교한 후 더 작으면 업데이트 
                distance[i[0]] = dis # i번째 노드까지 오는 비용 
                heapq.heappush(q, (dis, i[0]))     

    for i in range(1, v + 1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])

if __name__ ==  "__main__":
    main()