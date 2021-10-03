import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
board = []
max_value = -1 # 이후 계산을 줄이기 위해서 최댓값 알아두기 
for i in range(n):
    temp = list(map(int, input().split()))
    # max_value = max(max_value, max(temp))
    board.append(temp)

max_value = max(map(max, board)) # -> max값 계산하는 부분에서 메모리초과 발생 후에 max값 계산한다면 이런 방식으로 진행

answer = 0
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, value, count):
    global answer 

    if value + max_value * (4 - count) <= answer: # 남은 블럭 수가 최대인 경우라고 했을 때로 가정하여 계산한 경우 최대보다 작은 경우 제외 (가지치기!!!)
        return    

    if count == 4: # 4번 이동한 경우, 최댓값 넣기 
        answer = max(answer, value)
        return 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == 0:
            if count == 2: # ㅏ, ㅓ, ㅗ, ㅜ 모양 탐색하려면 새로 추가된 블럭을 방문 표시 및 더하고, 위치를 기존 위치로 넣어서 진행 
                visited[nx][ny] = 1
                dfs(x, y, value + board[nx][ny], count + 1)
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, value + board[nx][ny], count + 1)
            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, board[i][j], 1)
        visited[i][j] = 0
print(answer)   

