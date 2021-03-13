# dp값은 한번 정해지면 변하지 않아야한다. 
import sys 
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
n = int(input())

board = []
max_value = 0
mx = -1
my = -1

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] > max_value:
            mx = i
            my = j 
            max_value = temp[j]
    board.append(temp)

dp = [[0] * n for _ in range(n)] # 자기자신만 먹으므로 최소 1 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_value = 0

def dfs(x, y):
    print(x, y)
    global max_value
    if dp[x][y] == 0:
        dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if board[nx][ny] > board[x][y] and dp[nx][ny] < dp[x][y] + 1:
                dp[nx][ny] = max(dp[x][y] + 1, dp[nx][ny])

for i in range(n):
    for j in range(n):
        dfs(i, j)

print(dp)
print(max_value)
        