import sys
import copy

# bfs를 이용해보자.
input = sys.stdin.readline 

sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(): # 두 덩어리 이상인지 확인 
    visited = [[0] * m for _ in range(n)]

    count = 0

    def dfs(x, y):
        visited[x][y] = 1

        if 0 <= x - 1 < n and 0 <= y < m:
            if visited[x - 1][y] == 0 and board[x - 1][y] > 0:
                dfs(x - 1, y)
        if 0 <= x + 1 < n and 0 <= y < m:
            if visited[x + 1][y] == 0 and board[x + 1][y] > 0:
                dfs(x + 1, y)
        if 0 <= x < n and 0 <= y - 1< m:
            if visited[x][y - 1] == 0 and board[x][y - 1] > 0:
                dfs(x, y - 1)
        if 0 <= x < n and 0 <= y + 1 < m:
            if visited[x][y + 1] == 0 and board[x][y + 1] > 0:
                dfs(x, y + 1)
        
        

    for i in range(1, n - 1): # 첫번째랑 마지막 행, 열은 바다이므로 굳이 볼 필요 없음 
        for j in range(1, m - 1):
            if visited[i][j] == 0 and board[i][j] > 0:
                dfs(i, j)
                count += 1
                if count >= 2:
                    return True # 더 진행할 필요없으므로 

    return False 


count = 0

while not check(): # 두 덩어리 이상일 때까지!
    count += 1

    new_board = [[0] * m for _ in range(n)]
    
    for x in range(1, n - 1): # 빙산 업데이트 !
        for y in range(1, m - 1):
            if board[x][y] > 0:
                c = 0

                if 0 <= x - 1 < n and 0 <= y < m:
                    if board[x - 1][y] == 0:
                        c += 1
                if 0 <= x + 1 < n and 0 <= y < m:
                    if board[x + 1][y] == 0:
                        c += 1
                if 0 <= x < n and 0 <= y - 1< m:
                    if board[x][y - 1] == 0:
                        c += 1
                if 0 <= x < n and 0 <= y + 1 < m:
                    if board[x][y + 1] == 0:
                        c += 1

                v = board[x][y] - c
                if v > 0:
                    new_board[x][y] = v

    board = new_board

print(count)
