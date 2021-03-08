def solve():
    n = int(input())
    
    board = [[0] * n for _ in range(n)]
    number = 1
    x = 0
    y = -1

    d = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while number <= n * n:
        #print(x, y, d, number)
        tx = x + dx[d]
        ty = y + dy[d]

        if tx < 0 or tx >= n or ty < 0 or ty >= n or board[tx][ty] != 0:
            if d == 3:
                d = 0
            else:
                d += 1
        else:
            board[tx][ty] = number 
            x = tx 
            y = ty 
            number += 1

        #print(board)
    return board


def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1))
        for i in result:
            print(*i)

if __name__ ==  "__main__":
    main()