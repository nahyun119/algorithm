import sys 
import heapq

INF = 1e9
input = sys.stdin.readline 

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 단방향 

distance = [INF] * (n + 1)
hq = []
for e in graph[x]: # x에서 시작
    heapq.heappush(hq, (1, e)) # 모든 거리는 1이므로 
    distance[e] = 1 # 거리 1이므로 업데이트
distance[x] = 0 # 자기 자신은 0이므로


while hq:
    dis, node = heapq.heappop(hq)

    if distance[node] < dis:
        continue # 이미 최단거리로 업데이트 된 경우 
    
    for i in graph[node]: # node랑 이어진 거리
        cost = dis + 1 # 거리 동일하므로 
        if cost < distance[i]: # 최단 거리보다 작은 경우 
            distance[i] = cost 
            heapq.heappush(hq, (distance[i], i))


result = [x for x in range(1, n + 1) if distance[x] == k]
if len(result) == 0: # 답이 없다면 
    print(-1)
else:
    for r in result: # 오름차순 출력 
        print(r)