import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 7)

n = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
 
visited = [0 for i in range(n + 1)] # 방문여부 
parent = [0 for i in range(n + 1)] # 부모 정보 담는 곳 

def dfs(node):
    visited[node] = 1

    for i in graph[node]: # 연결된 노드 중에서 
        if visited[i] == 0: # 방문하지 않은 경우    
            parent[i] = node # i의 부모는 node
            visited[i] = 1
            dfs(i)


dfs(1)
for i in range(2, n + 1):
    print(parent[i])