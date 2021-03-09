T = int(input())
for t in range(T):
    n, s = map(str, input().split())
    n = int(n)

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    if s == 'up':
        for y in range(n):
            for x in range(n - 1):
                for i in range(x + 1, n):
                    if board[i][y] != 0 and board[x][y] != board[i][y]: # 0이 아닌 숫자가 중간에 있는경우 
                        break 
                    if board[x][y] == board[i][y] and board[x][y] != 0:
                        board[x][y] = board[x][y] * 2
                        board[i][y] = 0
                        break 
            temp = [0] * n
            idx = 0
            for k in range(n):
                if board[k][y] != 0:
                    temp[idx] = board[k][y]
                    idx += 1
            #print(temp)
            for k in range(n):
                board[k][y] = temp[k]
    
    if s == 'down':
        for y in range(n):
            for x in range(n - 1, 0, -1): # 아래에서 위 
                for i in range(x - 1, -1, -1):
                    #print(x, y, i, y)
                    if board[i][y] != 0 and board[x][y] != board[i][y]: # 0이 아닌 숫자가 중간에 있는경우 
                        break 
                    if board[x][y] == board[i][y] and board[x][y] != 0:
                        #print(y, x, y, i )
                        board[x][y] = board[x][y] * 2
                        board[i][y] = 0
                        break 
            temp = [0] * n
            idx = 0
            for k in range(n - 1, -1, -1):
                if board[k][y] != 0:
                    temp[idx] = board[k][y]
                    idx += 1
            #print(temp)
            for k in range(n - 1, -1, -1):
                board[k][y] = temp[n - k - 1]

    if s == 'left':
        for x in range(n):
            for y in range(n - 1):
                for i in range(y + 1, n):
                    if board[x][i] != 0 and board[x][y] != board[x][i]:
                        break 
                    if board[x][y] != 0 and board[x][y] == board[x][i]:
                        board[x][y] = board[x][y] * 2
                        board[x][i] = 0
                        break 
            temp = [0] * n
            idx = 0
            for k in range(n):
                if board[x][k] != 0:
                    temp[idx] = board[x][k]
                    idx += 1
            for k in range(n):
                board[x][k] = temp[k]
    
    if s == 'right':
        for x in range(n):
            for y in range(n - 1, 0, -1):
                for i in range(y - 1, -1, -1):
                    if board[x][i] != 0 and board[x][y] != board[x][i]:
                        break 
                    if board[x][y] != 0 and board[x][y] == board[x][i]:
                        board[x][y] = board[x][y] * 2
                        board[x][i] = 0
                        break 
            temp = [0] * n
            idx = 0
            for k in range(n - 1, -1, -1):
                if board[x][k] != 0:
                    temp[idx] = board[x][k]
                    idx += 1
            for k in range(n - 1, -1, -1):
                board[x][k] = temp[n - k - 1]
                
    print("#" + str(t + 1))
    for i in range(n):
        print(*board[i])
        
 