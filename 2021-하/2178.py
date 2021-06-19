import sys 
from collections import deque
input = sys.stdin.readline 

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(n):
    t = list(input().strip())
    graph[i] = [int(x) for x in t]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
visited = [[0] * m for i in range(n)]

queue.append((0, 0, 0))
visited[0][0] = 1

count = 0

while queue:
    x, y, count = queue.popleft()
    count += 1
    if x == n - 1 and y == m - 1: # 도착지인 경우 제일 먼저 도착지에 도착한 경우가 제일 최소 칸 수 이므로 !
        break # 종료 


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0: # 방문안한경우 
                if graph[nx][ny] == 1: # 이동할 수 있는 경우 
                    visited[nx][ny] = 1
                    queue.append((nx, ny, count))

print(count)

    