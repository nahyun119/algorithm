import sys
input = sys.stdin.readline 
from collections import deque 

n, m = map(int, input().split())
board = []

for i in range(n):
    row = list(input().strip())
    for j in range(m):
        if row[j] == 'R': # 빨간색 좌표
            red = (i, j)
        if row[j] == 'B': # 파란색 좌표
            blue = (i, j)
        if row[j] == 'O': # 구멍 좌표
            hole = (i, j)
    board.append(row)


queue = deque()
queue.append((red, blue, 0, red, blue, 0)) # 빨간색 좌표, 파란색 좌표, 이동 횟수 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def move(x, y, direc, another_x, another_y): # 구슬 이동하는 함수 (자기 자신 좌표랑 상대방 구슬 좌표)
    flag = False # 옆에 다른 색의 구슬이 있는지 여부 

    while board[x][y] != '#' and board[x][y] != 'O': # 벽과 구멍, 다른 색 구슬을 만나기 전까지 
        x = x + dx[direc]
        y = y + dy[direc] # 좌표 업데이트 

        if x == another_x and y == another_y:
            break 

    if flag: # 만난 경우 하나 더 빼기
        x -= dx[direc]
        y -= dy[direc]

    if board[x][y] == 'O': # 구멍인 경우 좌표 업데이트 안하고 그냥 
        return x, y
    
    return x - dx[direc], y - dy[direc]


def check(x, y, direc, another_x, another_y): # 가려는 방향에 다른 색 구슬이 있는지 확인
    flag = False # 옆에 다른 색의 구슬이 있는지 여부 

    while board[x][y] != '#' and board[x][y] != 'O':
        x = x + dx[direc]
        y = y + dy[direc]

        if x == another_x and y == another_y:
            flag = True
            break 
    
    return flag

answer = 1e9

while queue:
    r, b, count, pr, pb, d = queue.popleft()

    # print(r, b, pr, pb, d, count)

    if r == hole and b != hole: # 빨간색만 구멍을 통과한 경우 
        answer = min(answer, count)
        break     
    
    if r == hole and b == hole: # 빨간색, 파란색 모두 구멍을 통과한 경우 
        continue 

    if count > 10:
        count = -1
        break
    
    for i in range(4):
        nx = r[0] + dx[i] 
        ny = r[1] + dy[i] 

        bx = b[0] + dx[i]
        by = b[1] + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m: # 보드 안에 있는 경우     
            if board[nx][ny] != '#' or board[bx][by] != '#': # 벽만 아니면 된다 
                if check(r[0], r[1], i, b[0], b[1]): # 빨간색 구슬이 이동하는 방향에 파란색 구슬이 있는 경우 
                    cx, cy = move(b[0], b[1], i, r[0], r[1]) # 파란색 먼저 이동 
                    rx, ry = move(r[0], r[1], i, cx, cy)
                else: # 가려는 방향에 없는 경우     
                    rx, ry = move(r[0], r[1], i, b[0], b[1]) # 해당 방향으로 빨간색 이동 
                    cx, cy = move(b[0], b[1], i, rx, ry) # 해당 방향으로 파란색 이동 

                if not visited[rx][ry][cx][cy]:
                    visited[rx][ry][cx][cy] = True
                    queue.append(((rx, ry), (cx, cy), count + 1, r, b, i))


if answer == 1e9:
    print(-1)
else:
    print(answer)


    



            