import sys 
import copy
input = sys.stdin.readline 

n = int(input())
board = [[0] * 102 for _ in range(102)] # 102 * 102  격자 x, y가 100이 될 수 있음

def move(x, y, d, g, index):
    
    dx = [0, -1, 0, 1] # 오, 위, 왼, 아래 
    dy = [1, 0, -1, 0]

    ## 0세대 
    direc = d + 2 if d < 2 else d - 2
    stack = []
    stack.append(direc)
    
    current_x = x + dx[d] 
    current_y = y + dy[d] # 끝 점 좌표 
    board[current_x][current_y] = index

    for i in range(g):
        new_stack = copy.deepcopy(stack) # 이전 자취 방향 그대로 나와야하므로 
        # print(stack)
        while stack: # 이전 스택 확인
            direc = stack.pop()
            direc = 3 if direc == 0 else direc - 1 # 90도 방향으로 이동 
            current_x += dx[direc] # 끝 점 이동 
            current_y += dy[direc]  

            board[current_x][current_y] = index # 커브 표시 

            new_stack.append(direc + 2 if direc < 2 else direc - 2) # 반대 방향으로 넣기(끝점 기준에서 시작점으로 가는 방향이므로)
        
        stack = new_stack

for i in range(n):
    x, y, d, g = map(int, input().split())
    board[y][x] = i + 1 # 커브 표시 
    move(y, x, d, g, i + 1)

count = 0 
for i in range(101):
    for j in range(101):
        if board[i][j] != 0:
            if board[i + 1][j + 1] != 0 and board[i][j + 1] != 0 and board[i + 1][j] != 0:
                count += 1 
print(count)