import sys
import collections 
import itertools

input = sys.stdin.readline 

n, m = map(int, input().split()) # 행 열 

board = []
for i in range(n):
    board.append(list(map(int, input().split()))) # 보드 데이터 입력 

locations = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0: # 빈 칸인 경우에만 벽을 세울 수 있다. 
            locations.append((i, j)) # 가능한 좌표 위치

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(): # 바이러스 이동 
    visited = [[0] * m for i in range(n)] # 방문 표시 


    def dfs(x, y):
        visited[x][y] = 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
        
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0: 
                if board[nx][ny] == 0: # 방문하지 않고 빈 칸인 경우    
                    dfs(nx, ny) # visited 로 이미 방문 표시를 하므로 

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] == 2: # 방문 x, 바이러스인 경우 
                dfs(i, j)

    count = 0 
    for i in range(n): # 안전 영역 구하기
        #print(visited[i])
        
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] == 0: # 빈 칸이면서 바이러스 퍼지지 않은 경우     
                count += 1

    return count 

answer = 0

for location in list(itertools.combinations(locations, 3)):
    for l in location:
        board[l[0]][l[1]] = 1 # 벽으로 업데이트 

    answer = max(answer, move())

    for l in location:
        board[l[0]][l[1]] = 0 # 빈 칸으로 업데이트 

print(answer)