import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split()) # 노드 수, 간선 수, 시작점 

graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split()) # 양방향 
    graph[a].append(b)
    graph[b].append(a)

for i in range(n): # 정점번호 순서대로 진행해야하므로 
    graph[i].sort()

def go_dfs():
    global n, m, v, graph
    
    result = []
    visited = [0 for _ in range(n + 1)]
    
    def dfs(node):
        visited[node] = 1 # 방문 처리 
        result.append(node)

        for i in graph[node]: # 연결된 노드 
            if visited[i] == 0: # 방문하지 않았다면 
                dfs(i)

    dfs(v)
    print(*result)

def go_bfs():
    global n, m, v, graph

    result = []
    visited = [0 for i in range(n + 1)]

    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        node = queue.popleft()
        result.append(node)

        for i in graph[node]: # 연결된 노드 
            if visited[i] == 0: # 방문하지 않았다면 
                visited[i] = 1
                queue.append(i)

    print(*result)

go_dfs()
go_bfs()