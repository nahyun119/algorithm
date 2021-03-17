import sys
import copy
from collections import deque
input = sys.stdin.readline

## cctv 를 구현하는 부분이 너무 복잡하다! 줄여보자!! -> 15683-1.py
n, m = map(int, input().split())
board = []
cctv = []

cctv3 = [(0, 2), (0, 3), (1, 2), (1, 3)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if 1 <= temp[j] <= 5:
            cctv.append((i, j, temp[j]))
    board.append(temp)

total_cctv = len(cctv)

#print(cctv)
min_value = 1e9

def get_size(board): # 사각지대 범위 가져오기 
    value = 0
    for i in range(n):
        value += board[i].count(0)
    return value 

def dfs(board, index):
    global min_value
    if index >= total_cctv:
        #print(board)
        size = get_size(board)
        if min_value > size:
            min_value = size 
        return 

    pre_board = copy.deepcopy(board)
    x = cctv[index][0]
    y = cctv[index][1]
    number = cctv[index][2]

    if number == 1:
        queue = deque()
        
        for i in range(4):
            queue.append((x, y))

            while queue:
                cx, cy = queue.popleft()
                
                nx = cx + dx[i]
                ny = cy + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if -1 <= board[nx][ny] <= 5:
                        if board[nx][ny] == 0:
                            board[nx][ny] = -1 
                        queue.append((nx, ny))
            # print(board, index)
            dfs(board, index + 1)
            board = copy.deepcopy(pre_board)


    elif number == 2:
        queue = deque()

        for i in range(2):
            queue.append((x, y, -1))
            while queue:
                cx, cy, direc = queue.popleft()

                if direc == -1:
                    if i == 0:
                        direc1 = 0
                        nx1 = cx + dx[direc1]
                        ny1 = cy + dy[direc1]

                        direc2 = 1

                        nx2 = cx + dx[direc2]
                        ny2 = cy + dy[direc2]
                    else:
                        direc1 = 2
                        nx1 = cx + dx[direc1]
                        ny1 = cy + dy[direc1]

                        direc2 = 3

                        nx2 = cx + dx[direc2]
                        ny2 = cy + dy[direc2]

                    if nx1 >= 0 and nx1 < n and ny1 >= 0 and ny1 < m:
                        if -1 <= board[nx1][ny1] <= 5:
                            if board[nx1][ny1] == 0:
                                board[nx1][ny1] = -1
                            queue.append((nx1, ny1, direc1))

                    if nx2 >= 0 and nx2 < n and ny2 >= 0 and ny2 < m:
                        if -1 <= board[nx2][ny2] <= 5:
                            if board[nx2][ny2] == 0:
                                board[nx2][ny2] = -1
                            queue.append((nx2, ny2, direc2))
                    
                else:
                    nx = cx + dx[direc]
                    ny = cy + dy[direc]

                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if -1 <= board[nx][ny] <= 5:
                            if board[nx][ny] == 0:
                                board[nx][ny] = -1
                            queue.append((nx, ny, direc))
            # print(board, index)
            dfs(board, index + 1)
            board = copy.deepcopy(pre_board)

    elif number == 3:
        queue = deque()

        for i in range(4):
            queue.append((x, y, -1))
            while queue:
                cx, cy, direc = queue.popleft()

                if direc == -1:
                    d1, d2 = cctv3[i]

                    nx1 = cx + dx[d1]
                    ny1 = cy + dy[d1]

                    nx2 = cx + dx[d2]
                    ny2 = cy + dy[d2]

                    if nx1 >= 0 and nx1 < n and ny1 >= 0 and ny1 < m:
                        if -1 <= board[nx1][ny1] <= 5:
                            if board[nx1][ny1] == 0:
                                board[nx1][ny1] = -1
                            queue.append((nx1, ny1, d1))

                    if nx2 >= 0 and nx2 < n and ny2 >= 0 and ny2 < m:
                        if -1 <= board[nx2][ny2] <= 5:
                            if board[nx2][ny2] == 0:
                                board[nx2][ny2] = -1
                            queue.append((nx2, ny2, d2))
                else:
                    nx = cx + dx[direc]
                    ny = cy + dy[direc]

                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if -1 <= board[nx][ny] <= 5:
                            if board[nx][ny] == 0:
                                board[nx][ny] = -1
                            queue.append((nx, ny, direc))


            # print(board, index)
            dfs(board, index + 1)
            board = copy.deepcopy(pre_board)
    
    elif number == 4:
        queue = deque()

        for i in range(4):
            queue.append((x, y, -1))
            while queue:
                cx, cy, direc = queue.popleft()

                if direc == -1:
                    for j in range(4):
                        if i != j:
                            nx = cx + dx[j]
                            ny = cy + dy[j]

                            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                                if -1 <= board[nx][ny] <= 5:
                                    if board[nx][ny] == 0:
                                        board[nx][ny] = -1
                                    queue.append((nx, ny, j))
                            
                else:
                    nx = cx + dx[direc]
                    ny = cy + dy[direc]

                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if -1 <= board[nx][ny] <= 5:
                            if board[nx][ny] == 0:
                                board[nx][ny] = -1
                            queue.append((nx, ny, direc))
            
            # print(board, index)
            dfs(board, index + 1)
            board = copy.deepcopy(pre_board)
    
    elif number == 5:
        queue = deque()
        queue.append((x, y, -1))

        while queue:
            cx, cy, direc = queue.popleft()
            #print(cx, cy, direc, queue)
            if direc == -1:
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    
                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if -1 <= board[nx][ny] <= 5:
                            if board[nx][ny] == 0:
                                board[nx][ny] = -1
                            queue.append((nx, ny, i))
            else:
                nx = cx + dx[direc]
                ny = cy + dy[direc]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if -1 <= board[nx][ny] <= 5:
                        if board[nx][ny] == 0:
                            board[nx][ny] = -1
                        queue.append((nx, ny, direc))

        # print(board, index)
        dfs(board, index + 1)
        board = copy.deepcopy(pre_board)

dfs(board, 0)
print(min_value)
