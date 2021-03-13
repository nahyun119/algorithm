import heapq
import sys 
input = sys.stdin.readline
INF = 1e9
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c)) # 양방향이므로 

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0 # 자기 위치는 0으로 반드시 설정!!!!!
    q = []
    heapq.heappush(q, (0, start)) # 시작점을 넣는다
    while q:
        cost, node = heapq.heappop(q)

        if distance[node] < cost:
            continue

        for i in graph[node]:
            dis = cost + i[1]
            if distance[i[0]] > dis:
                distance[i[0]] = dis 
                heapq.heappush(q, (dis, i[0]))

    #print(distance)
    return distance

first_distance = dijkstra(1)
second_distance = dijkstra(v1)
third_distance = dijkstra(v2)

answer = min(first_distance[v1] + second_distance[v2] + third_distance[n], first_distance[v2] + third_distance[v1] + second_distance[n] )
if answer >= INF: # 바보야 INF 이상이겠지!!!!!! == 으로해서 계속 고민함,,
    print(-1)
else:
    print(answer)