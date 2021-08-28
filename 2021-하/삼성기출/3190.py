import sys
from collections import deque
input = sys.stdin.readline


n = int(input()) # 보드 크기
k = int(input())
apple_location = [] # 사과 위치
for i in range(k):
    x, y = map(int, input().split())
    apple_location.append((x - 1, y - 1))
l = int(input()) # 방향 변환 횟수 
 
direc_info = {} # 이후에 찾기 쉽도록 hash 이용 
for i in range(l):
    time, d = map(str, input().split())
    direc_info[int(time)] = d

# print(apple_location)
# print(direc_info)

snake = deque()
snake.append((0, 0)) # 맨 처음 위치 

direc = 1 # 처음에 오른쪽 방향
visited = [[0] * n for _ in range(n)] # 뱀이 있는 위치 표시 -> 뱀이랑 몸 부딪혔을때
visited[0][0] = 1

dx = [-1, 0, 1, 0] # 상 우 하 좌
dy = [0, 1, 0, -1]

count = 0

while True:
    x, y = snake.pop() # 현재 머리 위치

    if count in direc_info: # 방향 변환 정보 
        new_direc = direc_info[count]
        # print('hello', new_direc)
        if new_direc == 'L' : # 왼쪽으로 이동
            direc = 3 if direc == 0 else direc - 1
        if new_direc == 'D' : # 오른쪽으로 이동
            direc = 0 if direc == 3 else direc + 1 

    new_head = (x + dx[direc], y + dy[direc])
    # print(x, y, new_head, direc, count)
    if new_head[0] < 0 or new_head[0] >= n or new_head[1] < 0 or new_head[1] >= n : # 보드 밖으로 나간 경우
        count += 1
        break 

    if visited[new_head[0]][new_head[1]] == 1: # 이미 뱀 위치인 경우 
        count += 1
        break  

    snake.append((x, y)) # 원래 머리 넣고
    snake.append(new_head) # 새로운 머리를 넣는다.
    visited[new_head[0]][new_head[1]] = 1 # 몸 있다는거 표시 

    if new_head not in apple_location: 
        # 사과 없으면 꼬리도 이동 즉, 꼬리 popleft, 이미 먹은 사과는 삭제해야
        tx, ty = snake.popleft()
        visited[tx][ty] = 0 # 몸이 아니므로 업데이트 
    else:
        apple_location.remove(new_head) # 먹은 사과 삭제
    count += 1  

print(count)
