import sys 
from collections import deque
input = sys.stdin.readline


m, n, h = map(int, input().split())

graph = []
queue = deque()

for i in range(h):
    temp = []
    for j in range(n):
        t = list(map(int, input().split()))
        for k in range(m):
            if t[k] == 1: # 익은 토마토인 경우 
                queue.append((j, k, i, 0)) # x, y, z, 일 수 
        temp.append(t)
    graph.append(temp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while queue:
    x, y, z, day = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
            
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if graph[nz][nx][ny] == 0: # 익지않은토마토라면 
                graph[nz][nx][ny] = 1 # 익은 토마토로 변경 
                queue.append((nx, ny, nz, day + 1))


for i in range(h):
    for j in range(n):
        if graph[i][j].count(0) > 0:
            print(-1) # 모두 다 익지 못하는 경우 
            exit()

print(day)
