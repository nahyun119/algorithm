import copy
from collections import deque
T = int(input())

def dfs(step, board):
    global min_value

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if step == n:
        total = 0
        for i in range(h):
            total += w - board[i].count(0) # 남은 벽돌 수 
        
        if min_value > total:
            min_value = total
        return 

    
    for y in range(w):
        flag = False  # 그 다음 행 탐색을 방지하기 위해 
        for x in range(h):
            if board[x][y] == 0:
                continue
            else:
                graph = copy.deepcopy(board) # 나중에 폭발시키면 변하니까 복구하기위해서 
                q = deque()
                q.append((x, y, board[x][y]))

                while q:
                    x, y, cost = q.popleft()

                    if cost == 1: # 1이면 자기자신만
                        board[x][y] = 0
                    else:
                        board[x][y] = 0
                        for t in range(1, cost): # cost - 1만큼 연쇄 폭발 
                            for i in range(4):
                                nx = x + dx[i] * t
                                ny = y + dy[i] * t
                                
                                if nx >= 0 and nx < h and ny >= 0 and ny < w:
                                    if board[nx][ny] != 0 and (nx, ny, board[nx][ny]) not in q: # 중복피한다. 
                                        q.append((nx, ny, board[nx][ny]))

            ## 벽돌 정리 
            new_board = [[0] * w for _ in range(h)]
            for i in range(w):
                temp = []
                for j in range(h):
                    if board[j][i] != 0:
                        temp.append(board[j][i])
                for k in range(len(temp)):
                    new_board[h - len(temp) + k][i] = temp[k]
            flag = True 

            if flag:
                dfs(step + 1, new_board)
                board = graph
                break   

    dfs(n, board)




                                




for t in range(T):
    n, w, h = map(int, input().split())

    board = []
    # print(get_board(board, w, h))
    for _ in range(h):
        board.append(list(map(int, input().split())))

    min_value = 1e9
    dfs(0, board)

    print(min_value)