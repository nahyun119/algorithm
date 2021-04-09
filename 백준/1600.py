import sys 
from collections import deque
import copy
input = sys.stdin.readline 
k = int(input())
w, h = map(int, input().split()) # w 열 h 행 

board = []
for i in range(h):
    temp = list(map(int, input().split()))
    board.append(temp)


# 말 이동 
mx = [-2, -1, -2, -1, 2, 1, 2, 1]
my = [-1, -2, 1, 2, -1, -2, 1, 2]

# 그냥 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부
visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]
# 각 이동에 대해서 x, y에 대해 방문 했는지. 


q = deque()
q.append((0, 0, 0, k)) # x, y, count, k
visited[0][0][0] = 1

min_value = 1e9

while q:
    x, y, count, avail = q.popleft()
    # print(x, y, count, avail)
    
    if x == h - 1 and y == w - 1:
        if count < min_value:
            min_value = count 
        break 
    
    if avail > 0:
        for i in range(8):
            nx = x + mx[i]
            ny = y + my[i]

            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if visited[k - (avail - 1)][nx][ny] == 0 and board[nx][ny] == 0: # 말로 이동 
                    visited[k - (avail - 1)][nx][ny] = 1
                    q.append((nx, ny, count + 1, avail - 1))
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < h and ny >= 0 and ny < w:
            if avail > 0: # 말로 이동 가능한 
                if visited[k - avail][nx][ny] == 0 and board[nx][ny] == 0:
                    visited[k - avail][nx][ny] = 1
                    q.append((nx, ny, count + 1, avail))
            else: # 말 이동 횟수를 다 쓴 경우 
                if visited[k][nx][ny] == 0 and board[nx][ny] == 0:
                    visited[k][nx][ny] = 1
                    q.append((nx, ny, count + 1, avail))    

if min_value >= 1e9:
    print(-1)
else:
    print(min_value)