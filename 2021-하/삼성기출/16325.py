import sys 
from collections import deque
input = sys.stdin.readline 

n, m, k = map(int, input().split()) # n * n 땅 크기, m: 나무 수, k: 년 
food = [] # 겨울에 추가되는 양분 정보

for i in range(n):
    food.append(list(map(int, input().split())))


tree = [[[] for i in range(n)]  for _ in range(n)]
for i in range(m): # 나무 정보
    x, y, z = map(int, input().split()) # 나무 위치, 나이 
    tree[x - 1][y - 1].append(z) # 해당 위치에 여러 개의 나무가 존재할 수 있음 

# for i in range(n):
#     for j in range(n):
#         if tree[i][j]:
#             tree[i][j] = deque(sorted(tree[i][j]))

    
board = [[5] * n for _ in range(n)] # 현재 양분 정보. 맨 처음은 모두 5 
# 번식 
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, 0, -1, 1]

for i in range(k):
    ## 봄 
    dead_tree = [[[] for j in range(n)] for _ in range(n)] # 죽은 나무 정보 
    alive_tree = 0 # 살아있는 나무 수 

    for x in range(n):
        for y in range(n):
            if tree[x][y]: # 나무가 있는 경우   
                new_tree = [] # 새로운 나무 정보 
                tree[x][y].sort()
                for index, t in enumerate(tree[x][y]):
                    if t <= board[x][y]: # 양분을 줄 수 있는 경우 
                        new_tree.append(t + 1)
                        board[x][y] -= t 
                    else:
                        dead_tree[x][y] = tree[x][y][index:]
                        break 

                tree[x][y] = new_tree
                ## 여름 
                if dead_tree[x][y]:
                    for age in dead_tree[x][y]: # 봄 부분 진행한 후에 여름 진행해도 문제 x
                        board[x][y] += age // 2 

    ## 가을 & 겨울 
    for x in range(n):
        for y in range(n):
            if tree[x][y]: # 나무가 있는 경우
                for t in tree[x][y]:
                    if t % 5 == 0: # 나이가 5의 배수인 경우 번식
                        for i in range(8):
                            nx = x + dx[i]
                            ny = y + dy[i]

                            if 0 <= nx < n and 0 <= ny < n:
                                tree[nx][ny].append(1) # 인접한 8개의 칸에 나이 1인 나무 생성 
            ## 겨울 
            board[x][y] += food[x][y] # 양분 추가 



    # print("##########나무 정보##########")
    # print(tree)
    # print(board)

for x in range(n):
    for y in range(n):
        if tree[x][y]: 
            alive_tree += len(tree[x][y]) # 살아있는 나무 정보 추가 
            
print(alive_tree)
                         

                

        