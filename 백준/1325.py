import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, graph, n):
    q = deque()
    q.append(x)
    visited = [0] * (n + 1)
    dist = 0
    while q:
        cx = q.popleft()
        dist += 1
        for g in graph[cx]:
            if visited[g] == 0:
                q.append(g)
                visited[g] = 1
    return dist
    

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)

    max_value = 0
    result = []
    for i in range(1, n + 1):
        value = bfs(i, graph, n)
        if value > max_value:
            max_value = value
            result = []
            result.append(i)
        elif value == max_value:
            result.append(i)
    
    print(*result)
    

if __name__ ==  "__main__":
    main()