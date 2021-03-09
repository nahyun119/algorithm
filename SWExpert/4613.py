T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        temp = input().strip()
        board.append(list(temp))

    avail = []

    for i in range(1, n - 1): # 가능한 조합 수 
        for j in range(1, n - i):
            avail.append((i, j, n - (i + j)))

    min_value = 1e9

    for a in avail:
        w, b, r  = a
        w_total = 0
        for i in range(w):
            w_total += m - board[i].count('W')
        b_total = 0
        for i in range(w, b + w):
            b_total += m - board[i].count('B')

        r_total = 0
        for i in range(w + b, w+ b + r):
            r_total += m - board[i].count('R')

        #print(w, b, r, w_total, b_total, r_total)
        if min_value > w_total + b_total + r_total:
            min_value = w_total + b_total + r_total

    print("#" + str(t + 1), min_value)
    #print(min_value)