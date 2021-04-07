import sys 
from collections import deque
input = sys.stdin.readline 

r, c, n = map(int, input().split())

board = []
bomb = []

for i in range(r):
    temp = list(input().strip())
    for j in range(c):
        if temp[j] == 'O':
            bomb.append((i, j, 0)) # 시작부터 설치되므로 

    board.append(temp)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# print(bomb)
q = deque(bomb)

def bfs(queue, time):
    global board
    bomb_flag = False
    new_q = deque()
    while queue:
        x, y, t = queue.popleft()
        # print(x, y, t, time)
        # if board[x][y] == '.': # 폭탄 아니니까 넘긴다. 
        #     continue 
        
        if time - t == 3:
            board[x][y] = '.'
            bomb_flag = True 

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < r and ny >= 0 and ny < c:
                    board[nx][ny] = '.'
        else:
            if board[x][y] != '.':
                new_q.append((x, y, t))
    # print(new_q)
    return new_q, bomb_flag
        
def full(time):
    global board 
    global q
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = 'O'
                q.append((i, j, time))


for i in range(2, n + 1):
    full(i)
    q, flag = bfs(q, i)
    # print(board, i)
    # print(q, flag)
# print("==========")
for i in range(r):
    print(''.join(board[i]))





