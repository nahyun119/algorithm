def solve():
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    # tool = [[0] * m for _ in range(m)]

    max_value = 0
    for i in range(n):
        for j in range(n):
            value = 0
            if i + m >= 0 and i + m <= n and j + m >= 0 and j + m <= n:
                for k in range(m):
                    for u in range(m):
                        value += board[i + k][j + u]
                if value > max_value:
                    max_value = value
                print(i, j, value)
            # else:
            #     break
            
    return max_value           


def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()