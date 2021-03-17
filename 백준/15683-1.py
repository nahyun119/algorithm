import sys
import copy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
cctv = []


# cctv 가 갈 수 있는 방향! 
cctv_direc = [0,

[[0],[1],[2],[3]],

[[0,1],[2,3]],

[[1,2],[1,3],[0,2],[0,3]],

[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],

[[0,1,2,3]]]


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
    queue = deque()
    for direction in cctv_direc[number]:
        for i in direction:
            queue.append((x, y, i))

        while queue:
            cx, cy, direc = queue.popleft()

            nx = cx + dx[direc]
            ny = cy + dy[direc]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if -1 <= board[nx][ny] <= 5:
                    if board[nx][ny] == 0:
                        board[nx][ny] = -1
                    queue.append((nx, ny, direc))
        
        dfs(board, index + 1)
        board = copy.deepcopy(pre_board)

dfs(board, 0)
print(min_value)
