
def check(x, N):
    if(x >= 0 and x < N):
        return True
    else: 
        return False 

def main():
    N, M = map(int, input().split())

    cur_x, cur_y, cur_d = map(int, input().split())

    location = []
    for i in range(M):
        location.append(list(map(int, input().split())))

    footprint = [[0] * N for i in range(M)]

    footprint[cur_x][cur_y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    turn_time = 0
    # 맨처음에 시작하는 곳도 방문한 칸이므로 1로 초기화
    count = 1

    while True:

        #print(cur_x, cur_y, cur_d, turn_time)
        
        # 왼쪽으로 방향 바꾸기 
        if(cur_d == 0):
            cur_d = 3 
        else:
            cur_d -= 1

        # 방향을 변경할 때마다 +1 
        turn_time += 1 

        # 갈 수 있는 곳인지 확인 
        if(not check(cur_x + dx[cur_d], N) or not check(cur_y + dy[cur_d], M)):
            break

        # 육지이면서 가지 않은 곳인 경우 
        if(location[cur_x + dx[cur_d]][cur_y + dy[cur_d]] == 0 and footprint[cur_x + dx[cur_d]][cur_y + dy[cur_d]] == 0):
             cur_x += dx[cur_d]
             cur_y += dy[cur_d]
             footprint[cur_x][cur_y] = 1
             count += 1 
             # 이동했으므로 방향 바꾼 횟수 초기화 
             turn_time = 0

        # 이동하지 않고 방향 변경이 4번이나 이루어진 경우, 모두 다 가본 경우 
        if(turn_time == 4):
            # 뒤로 한칸 이동, 원래 이동하는 것과 반대로 이동 
            cur_x -= dx[cur_d]
            cur_y -= dy[cur_d]
            if(location[cur_x][cur_y] == 1):
                    break 
            # 방문한 칸 수를 출력하므로 갈 곳이 없어서 이동한 경우는 count에 추가 x         
            else: 
                footprint[cur_x][cur_y] = 1
                turn_time = 0
    print(count)

if __name__ ==  "__main__":
    main()    