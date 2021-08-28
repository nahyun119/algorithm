import sys
input = sys.stdin.readline 
n, m, x, y, k = map(int, input().split()) # 보드 크기, 처음 위치, 명령 수 

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

move = list(map(int, input().split())) # 이동 방향
# 마주보는면 -> 5에서 자기 자신 인덱스 제외한 면이 

dice = [0 for i in range(6)] # 주사위 면

def go(temp, direc): # 위 아래 왼 오 앞 뒤 
    new_dice = [] # 이동 
    if direc == 0: # 동으로 이동
        new_dice = [temp[2], temp[3], temp[1], temp[0], temp[4], temp[5]]
    if direc == 1: # 서로 이동
        new_dice = [temp[3], temp[2], temp[0], temp[1], temp[4], temp[5]]
    if direc == 2: # 북으로 이동
        new_dice = [temp[4], temp[5], temp[2], temp[3], temp[1], temp[0]]
    if direc == 3: # 남으로 이동
        new_dice = [temp[5], temp[4], temp[2], temp[3], temp[0], temp[1]]

    return new_dice

# 1: 동, 2: 서, 3: 북, 4: 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

current = 0 # 맨 처음 윗면은 0이므로 

for v in move:
    # print(current + 1, v, x, y, dice)
    x = x + dx[v - 1]
    y = y + dy[v - 1]
    if x >= 0 and x < n and y >= 0 and y < m: # 보드 범위 안에 있는 경우
        # 이동 
        dice = go(dice, v - 1) # 이동 
        if board[x][y] != 0: # 0이 아닌 경우
            dice[1] = board[x][y] # 아래 변경 
            board[x][y] = 0 # 복사 후 0으로 초기화
        else: # 0인 경우    
            board[x][y] = dice[1] # 주사위 수가 바닥면으로 복사 
        
        print(dice[0])
    else: # 범위 안에 없는 경우 이동하지 않고 다른 방향으로 
        x = x - dx[v - 1]
        y = y - dy[v - 1]
        continue