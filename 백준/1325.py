import sys 
from collections import deque 
input = sys.stdin.readline 
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(node):
    q = deque()
    count = 1
    visited = [0] * (n + 1)
    visited[node] = 1

    q.append(node)
    while q:
        v = q.popleft()
        count += 1 # 몇개의 노드를 해킹할 수 있는지 
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i) 

    return count 

max_value = -1
max_result = []

for i in range(1, n + 1):
    # print(graph[i])
    if len(graph[i]) > 0:
        result = bfs(i)
        # print(result)
        if max_value < result:
            max_result = [i]
            max_value = result 
        elif max_value == result:
            max_result.append(i)

print(*max_result)