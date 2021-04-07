# 가중치가 다르기 때문에 일반적인 BFS로 풀 수 없다. 따라서
# bfs를 활용한 다익스트라로 문제를 풀어보겠다..! 

import sys 
import heapq 
input = sys.stdin.readline 
INF = 1e9
MAX_NUM = 100000
n, k = map(int, input().split())

distance = [INF for _ in range(MAX_NUM + 1)] # 최대 10만

q = []
heapq.heappush(q, (0, n))
 
distance[n] = 0

while q:
    dis, number = heapq.heappop(q)

    if distance[number] < dis:
        continue
    
    avail = [(number - 1, 1), (number + 1, 1), (number * 2, 0)]
    for i in avail:
        if 0 <= i[0] <= MAX_NUM:
            cost = dis + i[1] # number까지 오는 거리 + number에서 다음 단계로 가는 거리 비용 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

print(distance[k])
    
  
    
