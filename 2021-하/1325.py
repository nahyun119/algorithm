import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())

graph = [[] for _ in range(n +  1)]
re = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split()) # a가 b를 신뢰하는 경우, b를 해킹하면 a를 해킹할 수 있다. a -> b
    graph[b].append(a)


def bfs(node):
    queue = deque()
    queue.append(node)
    visited = [0 for i in range(n + 1)]
    visited[node] = 1
    count = 1 # 해킹할 수 있는 컴퓨터 수 

    while queue:
        com = queue.popleft()
        for i in graph[com]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                count += 1
    
    return count 

result = -1
result_node = [] 
    

for i in range(1, n + 1):
    if parent[i] == i: # 부모가 없는 노드인 경우
        c = bfs(i)
        if c > result:
            result = c 
            result_node = [i]
        elif c == result:
            result_node.append(i)

print(*result_node)


    