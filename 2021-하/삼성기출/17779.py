import sys 
import itertools

input = sys.stdin.readline 

n = int(input())
population = []
for i in range(1, n + 1):
    population.append(list(map(int, input().split())))


#distance = list(itertools.product([x for x in range(1, n + 1)], [x for x in range(1, n + 1)]))

#print(distance)

distance = [(2, 2)]
for d1, d2 in distance:
    for x in range(1, n + 1):
        for y in range(1, n + 1): # 기준점 
            if x == 2 and y == 4:
                if 1 <= x + d1 + d2 <= n and (1 <= y - d1 and y - d1 < y + d2 and y + d2 <= n):
                    board = [[0] * (n + 1) for _ in range(n + 1)] # 선거구 표시 
                        
                    for dx in range(d1 + 1):
                        if 1 <= x + dx < n + 1 and 1 <= y - dx < n + 1:
                            if dx >= dy:
                            board[x + dx][y - dx] = 5
                        if 1 <= x + d2 + dx < n + 1 and 1 <= y + d2 - dx < n + 1: 
                            board[x + d2 + dx][y + d2 - dx] = 5

                    # for dy in range(d2 + 1):
                    #     if 1 <= x + dy < n + 1 and 1 <= y + dy < n + 1:
                    #         board[x + dy][y + dy] = 5
                    #     if 1 <= x + d1 + dy < n + 1 and 1 <= y - d1 + dy < n + 1:
                    #         board[x + d1 + dy][y - d1 + dy] = 5
                    if x == 2 and y == 4 and d1 == 2 and d2 == 2:
                        for i in range(1, n + 1):
                            print(*board[i])

                        
                    for x1 in range(1, n + 1):
                        for y1 in range(1, n + 1):
                            if 1 <= x1 < x + d1 and 1 <= y1 <= y: # 1번 선거구
                                if board[x1][y1] == 0:
                                    board[x1][y1] = 1 

                            if 1 <= x1 <= x + d2 and y < y1 <= n: # 2번 선거구 
                                if board[x1][y1] == 0:
                                    board[x1][y1] = 2
                            
                            if x + d1 <= x1 <= n and 1 <= y1 < y - d1 + d2: # 3번 선거구 
                                if board[x1][y1] == 0:
                                    board[x1][y1] = 3
                            
                            if x + d2 < x1 <= n and y - d1 + d2 < y1 <= n: # 4번 선거구 
                                if board[x1][y1] == 0:
                                    board[x1][y1] = 4 
                    
                    if x == 2 and y == 4 and d1 == 2 and d2 == 2:
                        for i in range(1, n + 1):
                            print(*board[i])



