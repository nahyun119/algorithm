import sys 
from collections import deque
input = sys.stdin.readline 

board = []
n, m = map(int, input().split())
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    visited = [[0] * m for _ in range(n)]

    count = 0 
    
    def bfs(x, y):
        queue = deque()
        visited[x][y] = 1
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if visited[nx][ny] == 0 and board[nx][ny] > 0:
                        visited[nx][ny] = 1  # 방문 표시를 먼저해주고 그 다음에 큐에 추가해준다. 
                        queue.append((nx, ny))
    

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if visited[i][j] == 0 and board[i][j] > 0:
                bfs(i, j)
                count += 1
                if count >= 2:
                    return True 

    return False 

count = 0 
flag = True 

while not check():
    count += 1

    new_board = [[0] * m for _ in range(n)]
    ice_count = 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if board[i][j] > 0:
                ice_count += 1
                c = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if board[nx][ny] == 0:
                            c += 1
                value = board[i][j] - c 
                if value > 0:
                    new_board[i][j] = value 

    if ice_count <= 0: # 남아있는 빙하가 모두 없는 경우 
        flag = False 
        break 

    board = new_board

if flag:
    print(count)
else:
    print(0)