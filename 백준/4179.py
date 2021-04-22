# queue에 이동 시간 같이 넣어서 하는 것보다 그냥 그래프에 표시해야 메모리 초과가 나지 않는다.
# 별로 차이가 없을 것 같은데도 큐에 넣고 안넣고의 차이가 크다 조심하자


import sys 
from collections import deque
input = sys.stdin.readline 

n, m = map(int, input().split())
fire = deque()
board = []
visited = [[0] * m for _ in range(n)]

for i in range(n):
    temp = list(input().strip())
    for j in range(m):
        if temp[j] == "J": # 시작 위치 
            start = (i, j)
            temp[j] = 0
        if temp[j] == "F": # 불 위치 
            fire.append((i, j))
            visited[i][j] = 1
    board.append(temp)


queue = deque()
queue.append((start[0], start[1])) # 초기 위치, 시간 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global fire, queue
    while queue:
        next_q = deque()

        while queue: # 사람 이동 
            x, y = queue.popleft()

            if board[x][y] == 'F': # 불이면 넘어가기 
                continue 

            if x == 0 or x == n - 1 or y == 0 or y == m - 1: # 가장자리인 경우 
                return board[x][y] + 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == '.':
                        next_q.append((nx, ny))
                        board[nx][ny] = board[x][y] + 1
        
        if not next_q: # 아무데도 갈 곳이 없는 경우 
            break
        
        queue = next_q
        
        next_f = deque()
        while fire: # 불 이동 
            x, y = fire.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m: # 다음 불 이동 업데이트 
                    if board[nx][ny] != '#' and visited[nx][ny] == 0:
                        next_f.append((nx, ny))
                        visited[nx][ny] = 1
                        board[nx][ny] = 'F'
        fire = next_f
        

result = bfs()
if result:
    print(result)
else:
    print("IMPOSSIBLE")