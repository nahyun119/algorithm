# 위상 정렬을 이용하는 문제 !!!! 
from collections import deque
import sys
input = sys.stdin.readline 
T = int(input())
result = []
for t in range(T):
    n, k = map(int, input().split()) 
    cost = [0] + list(map(int, input().split())) # 비용 
    graph = [[] for _ in range(n + 1)] 
    indegree = [0] * (n + 1)
    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    end = int(input())
    
    q = deque()
    dp = [-1] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = cost[i]
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            indegree[i] -= 1
            dp[i] = max(dp[node] + cost[i], dp[i])
            if indegree[i] == 0:
                q.append(i)

    result.append(dp[end])

for r in result:
    print(r)