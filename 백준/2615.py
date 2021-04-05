import sys
from collections import deque
input = sys.stdin.readline

board = []
stones = deque()
for i in range(19):
    temp = list(map(int, input().split()))
    for j in range(19):
        if temp[j] != 0:
            stones.append((i, j))
    board.append(temp)

visited = [[[0] * 4 for _ in range(19)] for _ in range(19)] # 방문 표시 0: 가로, 1: 세로, 2: 대각선 왼쪽, 3: 대각선 오른쪽 


flag = False 

while stones:
    x, y = stones.popleft()
    
    # print(x, y, visited[x][y])
    # 가로 탐색 
    c_count = 1
    if visited[x][y][0] == 0: # 해당 위치에서 가로 탐색을 하지 않은 경우 
        visited[x][y][0] = 1
        for i in range(1, 20):
            nx = x 
            ny = y + 1 * i
            if 0 <= nx < 19 and 0 <= ny < 19:
                if visited[nx][ny][0] == 0:
                    if board[nx][ny] == board[x][y]: # 다른거 등장하면 끝 
                        c_count += 1
                        visited[nx][ny][0] = 1 # 같은 걸로 탐색한 경우 해당 탐색 방문 표시 
                    else:
                        break 
            else:
                break 

    if c_count == 5:
        print(board[x][y])
        print(x + 1, y + 1)
        flag = True 
        break 

    # 세로 탐색 
    r_count = 1
    if visited[x][y][1] == 0: # 해당 위치에서 세로 탐색을 진행하지 않은 경우 
        visited[x][y][1] = 1
        for i in range(1, 20):
            nx = x + 1 * i 
            ny = y 
            if 0 <= nx < 19 and 0 <= ny < 19:
                if visited[nx][ny][1] == 0:
                    if board[nx][ny] == board[x][y]:
                        r_count += 1
                        visited[nx][ny][1] = 1 # 세로 탐색 방문 표시 
                    else: # 다른거 하면 끝 
                        break 
            else: # 범위 벗어나면 종료
                break 
    
    if r_count == 5:
        print(board[x][y])
        print(x + 1, y + 1)
        flag = True 
        break 

    # 대각선 왼쪽 
    l_count = 1 
    x_index = 22
    y_index = 22
    if visited[x][y][2] == 0: # 방문 안한 경우 
        # print(x,y)
        visited[x][y][2] = 1
        for i in range(1, 20):
            lx = x + 1 * i
            ly = y + (-1) * i

            if 0 <= lx < 19 and 0 <= ly < 19:
                if visited[lx][ly][2] == 0:
                    if board[lx][ly] == board[x][y]:
                        l_count += 1
                        visited[lx][ly][2] = 1
                        # print(x, y, lx, ly)
                        if y_index > ly: # 제일 왼쪽꺼를 출력해야하므로
                            x_index = lx
                            y_index = ly
                            # print(x_index + 1, y_index + 1)

                    else: # 다른거 나오면 탐색 종료 
                        break 
            else:
                break 

    if l_count == 5:
        print(board[x][y])
        print(x_index + 1, y_index + 1)
        flag = True 
        break 
    
    # 대각선 오른쪽 
    l_count = 1
    if visited[x][y][3] == 0:
        visited[x][y][3] = 1
        for i in range(1, 20):
            lx = x + 1 * i
            ly = y + 1 * i 

            if 0 <= lx < 19 and 0 <= ly < 19:
                if visited[lx][ly][3] == 0:
                    if board[lx][ly] == board[x][y]:
                        l_count += 1
                        visited[lx][ly][3] = 1
                    else:
                        break 
            else:
                break 

    if l_count == 5:
        print(board[x][y])
        print(x + 1, y + 1)
        flag = True 
        break 

if not flag:
    print(0)
