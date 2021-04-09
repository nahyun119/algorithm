import sys 
from collections import deque
input = sys.stdin.readline 
n, m = map(int, input().split())
graph = []
wall = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
            wall.append((i, j))
    graph.append(temp)

h, w, sx, sy, fx, fy = map(int, input().split())

sx -= 1
sy -= 1
fx -= 1
fy -= 1

q = deque()
q.append((sx, sy, 0)) # 이동 위치, 이동 횟수 

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_possible(x, y): # 직사각형 둘 수 있는지 없는지 확인 직사각형이 채워진 직사각형이 아니라 그냥 완전 네모 모서리만 확인하면 된다..
    # 가로 확인 
    for i in range(x, x + h):
        if 0 <= i < n:
            if graph[i][y] == 1:
                return False  
        else:
            return False  
        
        if 0 <= y + w - 1 < m:
            if graph[i][y + w - 1] == 1:
                return False
        else:
            return False 

    for i in range(y, y + w):
        if 0 <= i < m:
            if graph[x][i] == 1:
                return False 
        else:
            return False
        
        if 0 <= x + h - 1 < n:
            if graph[x + h - 1][i] == 1:
                return False 
        else:
            return False 
    return True

result = 1e9
while q:
    x, y, count = q.popleft()

    if x == fx and y == fy: # 도착하면 종료 
        if result > count:
            result = count 
        break 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m: # 격자판 위를 벗어나면 안된다. 
            if visited[nx][ny] == 0 and graph[nx][ny] == 0: # 방문도 안하고, 이동할 수 있는 경우 
                if is_possible(nx, ny): # 직사각형을 둘 수 있는지
                    visited[nx][ny] = 1
                    q.append((nx, ny, count + 1))
                else:
                    visited[nx][ny] = 1 # 어차피 못가니까 방문 처리 
                    continue

if result >= 1e9:
    print(-1)
else:
    print(result)