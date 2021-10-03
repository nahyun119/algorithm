import sys 
sys.setrecursionlimit(10**7)
input = sys.stdin.readline 
n, m, t = map(int, input().split()) 

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, value): # 인접한 애들 찾아서 변경하기
    global visited, board, flag
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = (y + dy[i]) % m

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0: 
                if board[nx][ny] == value:
                    flag = True 
                    board[x][y] = -1
                    board[nx][ny] = -1
                    dfs(nx, ny, value)
                    
for i in range(t):
    x, d, k = map(int, input().split())
    for j in range(1, n + 1): # 회전하기 
        order = x * j - 1 # 배수인 원판
        if order >= n: # 범위 밖인 경우
            break 
        new_circle = [0 for _ in range(m)]
        for index in range(m): # k칸만큼 이동 
            if d == 0: # 시계 방향
                new_circle[(index + k) % m] = board[order][index]
            else: # 반시계 방향
                new_circle[index - k] = board[order][index]
        board[order] = new_circle

    flag = False # 인접한 경우 플래그
    total = 0
    count = 0

    visited = [[0] * m for _ in range(n)]

    for x1 in range(n):
        for y1 in range(m):
            if board[x1][y1] != -1: # -1인 경우 숫자를 지운 경우 
                total += board[x1][y1]
                count += 1
                if visited[x1][y1] == 0:
                    dfs(x1, y1, board[x1][y1])
      
    if not flag and count > 0: # 인접한 수가 없는 경우 
        value = total / count 
        for x1 in range(n):
            for y1 in range(m):
                if board[x1][y1] != -1:
                    if board[x1][y1] > value:
                        board[x1][y1] -= 1
                    elif board[x1][y1] < value:
                        board[x1][y1] += 1

answer = 0

for i in range(n):
    for j in range(m):
        if board[i][j] != -1:
            answer += board[i][j]

print(answer)

        
