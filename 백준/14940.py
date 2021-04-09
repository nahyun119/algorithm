import sys 
from collections import deque
input = sys.stdin.readline 

n, m = map(int, input().split())
graph = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 2:
            start = (i, j)
    graph.append(temp)

q = deque()
q.append((start[0], start[1], 0))

visited = [[0] * m for _ in range(n)]
visited[start[0]][start[1]] = 1

distance = [[1e9] * m for _ in range(n)]

distance[start[0]][start[1]] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y, count = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny, count + 1))


for i in range(n):
    for j in range(m):
        if distance[i][j] >= 1e9 and graph[i][j] == 0: # 원래 벽인 부분은 0으로 출력 
            distance[i][j] = 0
        elif distance[i][j] >= 1e9 and graph[i][j] == 1: # 벽으로 인해서 못도달하는 곳은 -1 로 문제좀 제대로 읽자;;
            distance[i][j] = -1
    print(*distance[i])