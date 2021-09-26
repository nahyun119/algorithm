# 주석을 지우니 시간도 메모리도 짧아짐,..
import sys
import copy
input = sys.stdin.readline

r, c, t = map(int, input().split())

board = []
cleaner = []

flag = False # 공기청정기 발견 여부 

for i in range(r):
    temp = list(map(int, input().split()))
    if not flag:
        for j in range(c):
            if temp[j] == -1: # 공기청정기
                cleaner.append((i, j)) # 이어서 있으므로 
                cleaner.append((i + 1, j))
                flag = True 
    board.append(temp)

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

## 공기청정기 작동 
def move(order, directions):
    global board
    d_index = 0
    current_x = cleaner[order][0] + dx[directions[d_index]]
    current_y = cleaner[order][1] + dy[directions[d_index]]
    while current_x != cleaner[order][0] or current_y != cleaner[order][1]: # 공기청정기 위치로 돌아올 때까지
        if order == 0: # 위쪽 공기청정기라면 
            if current_x == 0 and current_y == 0: # 위로 다 올라온 경우 
                d_index += 1 # 오른쪽으로 
            elif current_x == 0 and current_y == c - 1: # 오른쪽으로 다 이동한 경우 
                d_index += 1 # 아래쪽으로 
            elif current_x == cleaner[order][0] and current_y == c - 1: # 아래로 다 이동한 경우 
                d_index += 1 # 왼쪽으로 
        else: # 아래쪽 공기청정기라면 
            if current_x == r - 1 and current_y == 0: # 아래로 다 이동한 경우 
                d_index += 1 # 오른쪽으로
            elif current_x == r - 1 and current_y == c - 1: # 오른쪽으로 다 이동한 경우 
                d_index += 1 # 위쪽
            elif current_x == cleaner[order][0] and current_y == c - 1: # 위로 다 이동한 경우 
                d_index += 1 # 왼쪽으로 

        nx = current_x + dx[directions[d_index]]
        ny = current_y + dy[directions[d_index]]

        # 먼지 이동 
        if nx == cleaner[order][0] and ny == cleaner[order][1]:
            board[current_x][current_y] = 0 # -1이 아니라 0으로 먼지 없애야함 
        else:
            board[current_x][current_y] = board[nx][ny]
        # 좌표 업데이트 
        current_x = nx
        current_y = ny 

for i in range(t):
    ## 미세먼지 확산
    new_board = [[0] * c for _ in range(r)] # 동시 업데이트이므로 board에 직접 업데이트하면 안됨. 
    for x in range(r):
        for y in range(c): 
            if board[x][y] == -1:
                new_board[x][y] = -1
            if board[x][y] > 0: # 미세먼지가 있는 경우 
                count = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] > -1: # 범위 밖, 공기청정기 있는 곳 확산 불가능 
                        new_board[nx][ny] += board[x][y] // 5 # 확산돼서 더하기 
                        count += 1

                new_board[x][y] += board[x][y] - board[x][y] // 5 * count 
    
    board = new_board
    # 위쪽 공기청정기는 반시계 방향으로 -> 시계 방향으로 돌면서 업데이트 
    move(0, [0, 1, 2, 3])
    # 아래 공기청정기는 시계 방향으로 -> 반시계 방향으로 돌면서 업데이트 
    move(1, [2, 1, 0, 3])

answer = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            answer += board[i][j]

print(answer)
