import sys
## 상어는 이동하다가 한 칸에 두 마리 이상이 있어도 가장 큰 상어가 다 잡아먹으므로 항상 칸 안에는 한 마리의 상어가 있다! 
input = sys.stdin.readline 

r, c, m = map(int, input().split()) # 크기, 상어 수 
shark_list = []

if m == 0: # 상어가 없는 경우 
    print(0)
    exit()

dx = [-1, 1, 0, 0] # 1: 위, 2: 아래, 3: 오 4: 왼
dy = [0, 0, 1, -1]

board = [[[] for _ in range(c)] for _ in range(r)]

for i in range(m):
    x, y, s, d, z = map(int, input().split()) # x, y, 속도, 이동 방향, 크기
    board[x - 1][y - 1].append((i, s, d, z)) # 상어 번호, 속도, 이동 방향, 크기 

current_y = -1 # 낚시왕이 있는 열, 열 한 칸 이동하고 시작하므로 

answer = 0 # 낚시왕이 잡은 상어 크기 합 

def change(direc):
    # 반대 방향 수정 
    if direc == 1: 
        direc = 2 
    elif direc == 2:
        direc = 1
    elif direc == 3:
        direc = 4
    else:
        direc = 3

    return direc 

for i in range(c):
    current_y += 1 # 낚시왕 열 이동

    for x in range(r): # 가장 가까운 상어 잡기 
        if board[x][current_y]: # 행 돌다가 상어를 만난 경우 
            s_i, s_s, s_d, s_z = board[x][current_y][0]
            answer += s_z # 크기 더하기
            board[x][current_y] = [] # 상어 사라짐 
            break # 가장 가까운거 하나이므로 종료 
    
    # 상어 이동 
    new_board = [[[] for _ in range(c)] for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if board[x][y]: # 상어가 있는 경우 
                index, speed, direc, size = board[x][y][0]
                #board[x][y] = [] # 초기화 
                
                cx = x 
                cy = y 

                # print("#####상어 처음 위치 확인#####")
                # print(index, cx, cy, direc)
                
                if direc == 1 or direc == 2: # 행 이동 
                    gap = cx if direc == 1 else r - 1 - cx # 위면 0이랑 아래면 행 끝이랑
                    
                    if gap >= speed: # 방향 전환이 없는 경우
                        cx = cx + dx[direc - 1] * speed
                        cy = cy + dy[direc - 1] * speed 
                    else: # 방향 전환
                        c_speed = speed - gap # gap만큼 이동 
                        cx = cx + dx[direc - 1] * gap
                        cy = cy + dy[direc - 1] * gap

                        move_cnt = c_speed // (r - 1) # 이동 횟수
                        remain_cnt = c_speed - ((r - 1) * move_cnt) # 나머지 이동 횟수 
                        #print(cx, cy, direc, move_cnt, remain_cnt)
                        if move_cnt % 2 != 0: # 홀수 번 
                            cx = 0 if cx == r - 1 else r - 1
                            direc = change(direc)
                        
                        if remain_cnt > 0: 
                            direc = change(direc)
                        #print(cx, cy, direc)
                        cx = cx + dx[direc - 1] * remain_cnt
                        cy = cy + dy[direc - 1] * remain_cnt
                else:
                    gap = cy if direc == 4 else c - 1 - cy # 왼쪽이면 
                    if gap >= speed: # 방향 전환이 없는 경우
                        cx = cx + dx[direc - 1] * speed
                        cy = cy + dy[direc - 1] * speed 
                    else: # 방향 전환
                        c_speed = speed - gap # gap만큼 이동 
                        cx = cx + dx[direc - 1] * gap
                        cy = cy + dy[direc - 1] * gap

                        move_cnt = c_speed // (c - 1) # 이동 횟수
                        remain_cnt = c_speed - ((c - 1) * move_cnt) # 나머지 이동 횟수 
                        
                        if move_cnt % 2 != 0: # 홀수 번 
                            cy = 0 if cy == c - 1 else c - 1
                            direc = change(direc)

                        if remain_cnt > 0: 
                            direc = change(direc)
                        
                        cx = cx + dx[direc - 1] * remain_cnt
                        cy = cy + dy[direc - 1] * remain_cnt

                # print("#####상어 마지막 위치 확인#####")
                # print(index, cx, cy, direc)

                if new_board[cx][cy]: # 이동한 곳에 상어가 있다면
                    if new_board[cx][cy][0][3] < size: # 원래 있던 애보다 크다면 업데이트
                        # print("#####원래 있던 애 확인####")
                        # print(new_board[cx][cy], [(index, speed, direc, size)])
                        new_board[cx][cy] = [(index, speed, direc, size)]
                else: # 없으면 그냥 넣기 
                    new_board[cx][cy].append((index, speed, direc, size))

    board = new_board # 상어 이동한 격자로 업데이트
    # print("############", i)
    # for i in range(r):
    #     print(*board[i])

print(answer)