n = int(input())
location = int(input())

board = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direc = 0
move = 1
number = 1
x = n // 2
y = n // 2


while number <= n * n:
    board[x][y] = number 
    if number == location:
        rx = x
        ry = y
    for i in range(move):
        x += dx[direc]
        y += dy[direc]
        number += 1
        if number > n * n:
            break
        if number == location:
            rx = x
            ry = y
        board[x][y] = number
    direc = (direc + 1) % 4
    if direc == 2: 
        move += 1
    if direc == 0:
        move += 1 

for i in range(n):
    print(*board[i])
print(rx + 1, ry + 1)

    
    