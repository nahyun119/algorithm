import sys
input = sys.stdin.readline

n = int(input())
bomb = []
for i in range(n):
    bomb.append(list(input().strip()))

board = []
for i in range(n):
    board.append(list(input().strip()))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


is_bomb = False 
for x in range(n):
    for y in range(n):
        if board[x][y] == 'x': # 눌린 곳
            if bomb[x][y] == '*': # 폭탄을 누른 경우 모든 폭탄을 다 표시해야한다. 
                board[x][y] = '*'
                is_bomb = True 
                continue # 폭탄 수를 구할 필요 없으므로 
            count = 0
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if bomb[nx][ny] == '*': # 폭탄이라면
                        count += 1
            board[x][y] = str(count)

# 폭탄이 눌린 경우
if is_bomb:
    for i in range(n):
        for j in range(n):
            if bomb[i][j] == '*':
                board[i][j] = '*'
            


for i in range(n):
    print(''.join(board[i]))


