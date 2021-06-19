import sys 
from collections import deque
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []

virus = deque()
avail_wall = [] # 새로 세울 수 있는 벽 조합 
for i in range(n):
    t = list(map(int, input().split()))
    for j in range(m):
        if t[j] == 0: # 빈 칸이므로 새로운 벽을 설치할 수 있다.
            avail_wall.append((i, j))
        elif t[j] == 2: # 바이러스 있는 곳 
            virus.append((i, j))

    graph.append(t)

avail = list(combinations(avail_wall, 3))
result = -1 # 안전영역 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(): # 바이러스 전파
    queue = deque(virus)
    change = [] # 변경된 부분 담기위해서 

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0: # 0인 경우 바이러스가 퍼질 수 있다. visited 안해도될 것 같다.
                    graph[nx][ny] = 2
                    change.append((nx, ny)) # 원래대로 돌리기위해서 변경된 부분 수정 
                    queue.append((nx, ny))
    
    count = get_safe(change)
    return count 
    
def get_safe(change): # 안전 영역 크기 확인하기
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 안전 영역인 경우 
                count += 1
            if (i, j) in change: # 변경된 부분이라면 (즉 바이러스로 변한 곳이라면)
                graph[i][j] = 0 # 변경해주기 

    return count 

for a in avail:
    for x, y in a: # 벽 설치
        graph[x][y] = 1 # 벽으로 변경 
    count = bfs() # 바이러스 전파 및 안전 영역 계산 
    if count > result:
        result = count
    for x, y in a:
        graph[x][y] = 0 # 다시 변경
        
print(result)
