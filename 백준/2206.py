# 벽을 뚫고 온 거리랑 벽을 뚫고 오지 않은 거리를 모두 계산 

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, list(input().strip()))))

queue = deque()
queue.append((0, 0, 0))

visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
# visited[x][y][0] : 벽을 안뚫고 온 경우 거리  
# visited[x][y][1] : 벽을 뚫고 온 거리 
visited[0][0][0] = 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, w = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny][w] == -1: # 벽을 뚫고 온 경우 or 벽을 뚫은 경우가 아닌 경우에 + 1
                visited[nx][ny][w] = visited[x][y][w] + 1
                queue.append((nx, ny, w))
            elif w == 0 and graph[nx][ny] == 1 and visited[nx][ny][1] == -1: #벽을 안뚫고왔는데, 벽이 있는 경우 
                visited[nx][ny][1] = visited[x][y][w] + 1
                queue.append((nx, ny, 1))
        
dis1, dis2 = visited[n - 1][m - 1][0], visited[n - 1][m - 1][1]
#print(visited)
if dis1 == -1 and dis2 != -1:
    print(dis2)
elif dis1 != -1 and dis2 == -1:
    print(dis1)
else:
    print(min(dis1, dis2))