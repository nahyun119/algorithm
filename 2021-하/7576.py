import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

graph = []
queue = deque()

for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

    for j in range(m):
        if temp[j] == 1: # 익은 토마토 위치
            queue.append((i, j, 0)) # 위치, 일 수 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]   

while queue:
    x, y, day = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0: #익지 얂은 토마토인 경우 
                graph[nx][ny] = 1 # 익은 상태로 변경
                queue.append((nx, ny, day + 1))

def check():
    for i in range(n):
        if graph[i].count(0) > 0: # bfs 왼료했는데 0이 있는 경우, 토마토가 모두 익을 수 없는 경우 
            return False 
    return True 

if check():
    print(day)
else:
    print(-1)

