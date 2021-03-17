# 으아아아아ㅏㅏ아아아 너무 어려워ㅠ 
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = []

for i in range(n):
    temp = list(input().strip())
    for j in range(m):
        if temp[j] == 'B':
            blue = (i, j)
        elif temp[j] == 'R':
            red = (i, j)
    board.append(temp)

min_value = 1e9

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def go(x, y, direc, board):
    queue = deque()
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()

        nx = cx + dx[direc]
        ny = cy + dy[direc]

        if board[nx][ny] == 'O':
            return nx, ny

        if board[nx][ny] != '#':
            queue.append((nx, ny))
    
    return cx, cy

    


def dfs(rx, ry, bx, by, board, count):
    global min_value
    
    if count == 1:
        print(rx, ry, bx, by, board[rx][ry])
    if board[rx][ry] == 'O' and board[bx][by] != 'O':
        if min_value > count:
            min_value = count
            return 
    if board[rx][ry] == 'O' and board[bx][by] == 'O':
        return

    if count > 10:
        return 
        
    else:

        for i in range(4):
            nx, ny = go(rx, ry, i, board) # 빨간색 이동 
            mx, my = go(bx, by, i, board) # 파란색 이동 
            print(nx, ny, mx, my, i)
            if nx == rx and ny == ry and my == by and mx == bx: 
                continue # 이동해도 동일한 경우는 이동하지 dfs 진행 x 
            else:

                if board[nx][ny] == 'O':
                    pre_red = board[rx][ry]
                    pre_blue = board[bx][by]

                    board[rx][ry] = '.'

                    pre_blue = board[bx][by]
                    pre_new_blue = board[mx][my]
                    board[mx][my], board[bx][by] = board[bx][by], board[mx][my]

                    dfs(nx, ny, mx, my, board, count + 1)
                    board[mx][my] = pre_new_blue
                    board[bx][by] = pre_blue
                    board[rx][ry] = pre_red

                else:
                    pre_red = board[rx][ry]
                    pre_new_red = board[nx][ny]
                    board[nx][ny], board[rx][ry] = board[rx][ry], board[nx][ny]

                    pre_blue = board[bx][by]
                    pre_new_blue = board[mx][my]
                    board[mx][my], board[bx][by] = board[bx][by], board[mx][my]

                    dfs(nx, ny, mx, my, board, count + 1)

                    board[nx][ny] = pre_new_red
                    board[rx][ry] = pre_red
                    board[mx][my] = pre_new_blue
                    board[bx][by] = pre_blue
                

dfs(red[0], red[1], blue[0], blue[1], board, 0)
print(min_value)



                    
