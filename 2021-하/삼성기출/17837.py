import sys 

input = sys.stdin.readline 

n, k = map(int, input().split()) # 체스판 크기, 말의 수 
board = []
for i in range(n):
    board.append(list(map(int, input().split()))) # 0: 흰, 1: 빨, 2: 파


locations = [[[] for _ in range(n)] for _ in range(n)] # 말의 현재 위치 
horse = [] # 말 순서대로 정보 

for i in range(k):
    x, y, direc = map(int, input().split())
    horse.append([i + 1, x - 1, y - 1, direc])
    locations[x - 1][y - 1].append(i + 1)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def change(direc):
    if direc == 1:
        return 2
    if direc == 2:
        return 1
    if direc == 3:
        return 4
    if direc == 4:
        return 3

# 파란색이나 체스 밖 범위라서 이동을 못하는 경우에 방향을 한번 더 바꾸고 진행을 하는데,
# 이 때 방향을 바꿔서 이동한 칸의 색에 따라서 이동하는 방법이 달라진다. 
# 원래는 그냥 윗 말들 다같이 그대로 옮겨가는줄 알았는데, 그게 아니라 이동하려는 칸에 따라서 달라진다. 흰 색이면 그대로, 빨간색이면 반대로
# 파란색, 체스 밖인 경우는 이동하지 않고 그대로(이전과 방향만 달라진 상태)

def move(flag, index):
    global locations

    h_index, x, y, direc = horse[index]

    nx = x + dx[direc - 1]
    ny = y + dy[direc - 1]

    if 0 <= nx < n and 0 <= ny < n: # 체스판 범위 내
        current_index = locations[x][y].index(h_index)
        if board[nx][ny] != 2: # 흰 색 혹은 빨간색인 경우 
            locations[nx][ny] += locations[x][y][current_index:] if board[nx][ny] == 0 else locations[x][y][current_index:][::-1]
            if len(locations[nx][ny]) >= 4: # 게임 종료 
                print(count + 1)
                exit()
            for n_index in locations[x][y][current_index:]:
                horse[n_index - 1][1] = nx 
                horse[n_index - 1][2] = ny # 말 정보 업데이트 

            locations[x][y] = locations[x][y][:current_index] # 새로 업데이트 
        else:
            if flag: # 이미 한 번 파란색 혹은 체스 밖에서 온 경우   
                return # 이동하지 않고 리턴 
            
            direc = change(direc)
            horse[index][3] = direc # 방향 업데이트     
             
            move(True, index)
    else:
        if flag:
            return 

        direc = change(direc)
        horse[index][3] = direc      
        move(True, index)


count = 0
while count <= 1000: # 1000 이상인 경우 -1 
    for i in range(k):
        move(False, i)
    
    count += 1
print(-1)     

