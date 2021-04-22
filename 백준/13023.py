import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, visited):
    visited.add(node)
    if len(visited) >= 5:
        print(1)
        exit()

    for e in graph[node]:
        if e not in visited:
            dfs(e, visited)

    visited.remove(node) # 백트래킹해서 한 번에 갈 수 있는지를 파악할 수 있도록 한다.

for i in range(n):
    dfs(i, set([]))

print(0)  
