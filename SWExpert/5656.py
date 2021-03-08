# 으으아으ㅏ으아ㅡ아ㅡ아아아 너무 어렵다 ㅠ

from collections import deque
import sys

sys.setrecursionlimit(10**6)

def dfs(x, y, value, graph, w, h):
    graph[x][y] = 0

    if value <= 0:
        return 

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < h and ny >= 0 and ny < w:
            if graph[nx][ny] != 0:
                dfs(nx, ny, value - 1 + graph[nx][ny], graph, w, h)


def get_start(w, h, board, step): # 시작 위치 가져오는 함수 
    q = deque()
    max_value = 0
    for i in range(w):
        for j in range(h):
            if board[j][i] != 0:
                q.append((j, i, step, board[:]))
                break 
    
    return q

def get_board(board, w, h): # 벽돌 정리 
    for i in range(w):
        col = [board[x][i] for x in range(h)]
        if col.count(0) < h:
            while col.count(0) > 0:
                col.remove(0)
            t = h - len(col)
            for j in range(h):
                if j < t:
                    board[j][i] = 0
                else:
                    board[j][i] = col[j - t]
            
    return board 



T = int(input())
for t in range(T):
    n, w, h = map(int, input().split())

    board = []
    # print(get_board(board, w, h))
    for _ in range(h):
        board.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    start = get_start(w, h, board, 0)
    min_value = 1e9
    # print(start)
    while start:
        x, y, step, graph = start.popleft() 
        #print(x, y, step, graph)
        if step == n:
            # total = 0
            # for i in range(h):
            #     print(graph[i])
            #     total += w - graph[i].count(0)
            # if total < min_value:
            #     min_value = total
            continue
        dfs(x, y, graph[x][y] - 1, graph, w, h)
        print(x, y, step)
        for i in range(h):
            print(graph[i])
        new_board = get_board(graph, w, h)
        start.extend(get_start(w, h, new_board, step + 1))

    print(min_value)




