from collections import deque
def main():
    N = int(input())

    board = [[0] * N for _ in range(N)]

    # 맨 처음이 1, 1로 되어있으므로 
    K = int(input())
    for i in range(K):
        x, y = map(int, input().split())
        board[x -1][y-1] = 1
     
    L = int(input())

    direction = deque()
    snake = deque()
    for i in range(L):
        x, y = input().split()
        direction.append((int(x),y))
    # 동 :0, 남: 1, 서: 2, 북: 3
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    count = 0
    x = 0
    y = 0
    c_dir = 0
    
    snake.append((x, y))
    tail = (0,0)
    # 벽에 부딪히지 않고, 자기 자신 부딪힌 경우 
    while True:
        #print(x, y, c_dir, tail)
        nx = x + dx[c_dir]
        ny = y + dy[c_dir]
        count += 1
        if nx < 0 or nx >= N or ny >= N or ny < 0:
            print(count)
            return
        # 자기 자신 부딪힌 경우 
        if (nx, ny) in snake:
            print(count)
            return 
        if board[nx][ny] == 1:
            snake.append((nx, ny))
            #snake[nx][ny] = 1
            board[nx][ny] = 0
            x = nx
            y = ny
        else:
            # snake[nx][ny] = 1
            snake.append((nx, ny))
            snake.popleft()
            x = nx
            y = ny
        # 방향 정보가 있는 경우 
        if direction and direction[0][0] == count:
            if direction[0][1] == 'D': # 오른쪽 이동 
                if c_dir == 3:
                    c_dir = 0
                else:
                    c_dir += 1
            if direction[0][1] == 'L': # 완쪽 이동 
                if c_dir == 0:
                    c_dir = 3
                else:
                    c_dir -= 1
            direction.popleft() # 방향 정보 제거     
        
        
    print(count)

if __name__ ==  "__main__":
    main()