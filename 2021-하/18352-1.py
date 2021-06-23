# 모든 거리가 동일한 경우 bfs를 해서 가장 먼저 도달한 것이 최적, 최단
# 그러므로 그냥 bfs를 진행하면 된다. 모든 거리는 1로 동일하므로 

import sys
from collections import deque 
INF = 1e9
input = sys.stdin.readline 

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque()
distance = [INF] * (n + 1)

queue.append((x, 0)) # 시작 노드 
distance[x] = 0

result = []

while queue:
    node, dis = queue.popleft()

    for e in graph[node]:
        if distance[e] >= INF: #방문을 하지 않았다면 
            distance[e] = dis + 1 # 방문 표시 
            if distance[e] < k:
                queue.append((e, distance[e]))
            if distance[e] == k: # k라면 
                result.append(e)

if result: # 결과가 있다면 
    result.sort()
    for r in result: 
        print(r)
else:
    print(-1)