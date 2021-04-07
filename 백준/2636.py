import sys 
from collections import deque
input = sys.stdin.readline 
sys.setrecursionlimit(10 ** 7)
n, m = map(int, input().split())
board = []
q = deque()
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
            q.append((i, j))
    board.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def check_air(): # 공기 체크 가장 자리에서 갈 수 있는 곳 변경 
    global board
    visited = [[0] * m for _ in range(n)]

    def dfs(x, y):
        visited[x][y] = 1
        board[x][y] = 2 # 공기라고 체크 

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if board[nx][ny] != 1 and visited[nx][ny] == 0:
                    dfs(nx, ny)
    

    for i in range(0, n, n - 1):
        for j in range(m):
            if board[i][j] != 1 and visited[i][j] == 0:
                dfs(i, j)

    for i in range(0, m, m - 1):
        for j in range(n):
            if board[j][i] != 1 and visited[j][i] == 0:
                dfs(j, i)



def bfs(queue):
    global board
    new_q = deque()
    change_q = deque()
    while queue:
        x, y = queue.popleft()
        # print(x, y)
        flag = True 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if board[nx][ny] == 2: # 공기라면 녹는다.
                    flag = False 
                    break 
        if flag: # 안 녹는 애들만 다시 넣는다. 
            new_q.append((x, y))
        else: # 녹는 애들만 따로 담는다. 후에 board 변경하기 위해서 
            change_q.append((x, y))
    
    while change_q: # 2 공기로 업데이트 
        x, y = change_q.popleft()
        board[x][y] = 2
    
    return new_q

time = 0
pre_cheeze = 0
while q:
    pre_cheeze = len(q)
    check_air()
    q = bfs(q)
    time += 1
    # print(q)
    # for i in range(n):
    #     print(board[i])
print(time)
print(pre_cheeze)
