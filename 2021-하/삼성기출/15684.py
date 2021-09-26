import sys 

input = sys.stdin.readline 

n, m, h = map(int, input().split())

board = [[0] * (n - 1) for _ in range(h)] # 사다리 있는지 없는지 

for i in range(m): # 가로선 정보
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1 # 가로선 연속이 경우, 접하는 경우에 가로선을 놓을 수 없음. 

## 사다리타기 
def move(): 
    for i in range(n): 
        current_y = i #(0, i)에서 시작 
        
        for current_x in range(h):
            if 0 <= current_y < n - 1 and  board[current_x][current_y] == 1: # 오른쪽으로 이동 
                current_y += 1
            elif current_y > 0 and board[current_x][current_y - 1] == 1: # 왼쪽으로 이동 
                current_y -= 1

        if current_y != i: # 다르다면 더이상 보지 않고 종료 
            return False 

    return True 

answer = 1e9

def set_ladder(x, y, count):
    global board, answer

    if move(): # 사다리 놓고나서 성공한 경우 
        answer = min(answer, count)
        return 

    if count >= 3 or answer <= count: # 사다리 다 놓은 경우 or 카운트가 답보다 큰 경우 볼 필요 없음. >= 3 해야 시간초과 안난다...
        return 

    for i in range(x, h): # 가로선부터 계속 0부터 탐색할 필요 없으므로 
        current_y = 0 # 행 바뀌면 처음부터 탐색 
        if i == x:
            current_y = y # 차례대로 탐색
        for j in range(current_y, n - 1):
            if board[i][j] == 1 or (j > 0 and board[i][j - 1] == 1) or (0 <= j + 1 < n - 1 and board[i][j + 1] == 1):
                continue 
            else: # 사다리를 놓을 수 있는 곳이라면 
                board[i][j] = 1 
                set_ladder(i, j + 2, count + 1) # 연속된 부분은 굳이 볼 필요가 없으므로
                board[i][j] = 0 # 백트래킹 
            
set_ladder(0, 0, 0)
print(answer if answer < 4 else -1)