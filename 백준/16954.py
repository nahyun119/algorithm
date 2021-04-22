import sys
from collections import deque
input = sys.stdin.readline 

board = []
walls = []
for i in range(8): # 8 * 8 체스판
    temp = list(input().strip())
    for j in range(8):
        if temp[j] == "#":
            walls.append((i, j))


queue = deque()
queue.append((7, 0, walls)) # 가장 왼쪽 아래가 시작

visited = [[0] * 8 for _ in range(8)]
visited[7][0] = 1

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

 
def move(wall): # 벽 아래로 한 칸씩 내리기 
    temp = []
    for x, y in wall: 
        if x + 1 < 8: # 범위 안에 있다면
            temp.append((x + 1, y))

    return temp 

flag = False 

while queue:
    x, y, w = queue.popleft()

    # if (x, y) in w:
    #     continue
     
    if x == 0 and y == 7: # 가장 오른쪽 위! 
        flag = True 
        break 

    new_walls = move(w) # 이동하기 전 미리 그 다음 벽 상태 구하기 

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
            if visited[nx][ny] == 0 and (nx, ny) not in w and (nx, ny) not in new_walls: # 방문 안하고 벽이 아닌 경우, 다음 벽 상태에서도 벽이 아닌 경우 
                queue.append((nx, ny, new_walls)) # 이동하고 벽 이동 
                visited[nx][ny] = 1 # 방문처리

    if (x, y) not in new_walls: # 벽이 아닌 경우 
        queue.append((x, y, new_walls)) # 이동안하고 계속 서있는 경우 

if flag:
    print(1)
else:
    print(0)
      
    
