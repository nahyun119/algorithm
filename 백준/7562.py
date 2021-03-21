import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())
    cx, cy = map(int, input().split())
    ex, ey = map(int, input().split())

    dx = [-2, -1, -2, -1, 1, 2, 1, 2]
    dy = [-1, -2, 1, 2, -2, -1, 2, 1]

    visited = [[0] * n for _ in range(n)]

    visited[cx][cy] = 1
    
    queue = deque()
    queue.append((cx, cy, 0))

    while queue:
        x, y, count = queue.popleft()

        if x == ex and y == ey:
            break 

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if visited[nx][ny] == 0:
                    queue.append((nx, ny, count + 1))
                    visited[nx][ny] = 1
    
    print(count)