import sys 

input = sys.stdin.readline 

n, m = map(int, input().split())
current_r, current_c, current_d = map(int, input().split())

dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1]

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

visited = [[0] * m for i in range(n)] # 청소기가 청소한 곳 

count = 0 

while True:
    if visited[current_r][current_c] == 0: # 후진 같은 경우, 겹치므로 
        count += 1

    visited[current_r][current_c] = 1 # 청소
    flag = False # 청소할 곳이 있는 경우 
    nd = current_d
    
    for i in range(4):
        nd = 3 if nd == 0 else nd - 1
        nx = current_r + dx[nd]
        ny = current_c + dy[nd]

        if board[nx][ny] == 0 and visited[nx][ny] == 0: # 청소할 수 있는 곳이라면
            current_r = nx
            current_c = ny 
            current_d = nd 
            flag = True 
            break

    if not flag:
        # 네 방향 다 청소했거나 벽인 경우, 후진  
        nx = current_r - dx[current_d]
        ny = current_c - dy[current_d]

        if board[nx][ny] == 0: # 벽이 아닌 경우 
            current_r = nx 
            current_c = ny 
        else:
            break 
print(count)
