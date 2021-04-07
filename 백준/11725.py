import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(10 ** 7)

n = int(input())

# dfs를 이용해서 풀어보자 

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
parent = [x for x in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    visited[node] = 1
    # print(node)
    for v in graph[node]: # node와 이어진 애들 
        if visited[v] == 0:
            parent[v] = node # node가 부모가 된다. 
            dfs(v)

dfs(1)
for i in range(2, n + 1):
    print(parent[i])

         


