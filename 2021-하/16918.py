import sys
from collections import deque
input = sys.stdin.readline 

r, c, n = map(int, input().split())
graph = []

queue = deque()
bomb = [[-1] * c for _ in range(r)] # 원래 설치된 폭탄 말고 다 1초이므로, 설치 시간 표시 


for i in range(r):
    t = list(input().strip())
    for j in range(c):
        if t[j] == 'O': # 폭탄이 있는 경우 
            queue.append((i, j)) # x, y
            bomb[i][j] = 0 # 설치 시간 표시 
        
    graph.append(t)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(time):
    new_bomb = deque()
   
    while queue:
        x, y = queue.popleft()
        if bomb[x][y] == -1: # 폭탄 설치했다가 다른 폭탄으로 인해 폭탁이 없어진 경우는 넘어가야한다. queue에는 이미 다 있으므로 
            continue 
        
        if bomb[x][y] + 3 == time: # 폭탄이 터지는 시간인 경우   
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c:
                    if bomb[nx][ny] > bomb[x][y]: # 같은 경우 동시에 터지는 폭탄을 의미하므로 초기화하면 안된다. 
                        bomb[nx][ny] = -1 # 폭탄이 터져서 빈 칸이 되므로 설치시간 초기화 
                        graph[nx][ny] = '.' # 빈칸으로 초기화

            # 다른 폭탄을 검증 후에 원래 자리를 수정 
            bomb[x][y] = -1 # 설치된 곳도 초기화 
            graph[x][y] = '.' # 빈칸으로 초기화
        else: # 폭탄이 아직 터지는 시간이 아닌 경우, 다시 queue에 담는다. 
            new_bomb.append((x, y))

    return new_bomb

def make_bomb(time): # 폭탄 설치
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.': # 빈칸인 경우 폭탄 설치
                graph[i][j] = 'O'
                bomb[i][j] = time 
                queue.append((i, j))
                 

for i in range(2, n + 1):
    if i % 2 == 0:
        make_bomb(i) # 폭탄 설치 
    new = bfs(i)
    queue = new

for i in range(r):
    print(''.join(graph[i]))