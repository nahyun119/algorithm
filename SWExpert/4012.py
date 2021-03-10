T = int(input())
for t in range(T):
    n = int(input())
    food = []
    for i in range(n):
        food.append(list(map(int, input().split())))
    
    s = [[0] * n for _ in range(n)] 

    # n // 2개 조합 

    for i in range(n):
        for j in range(i + 1, n):
            value = food[i][j] + food[j][i]
            s[i][j] = value 
            #s[j][i] = value
    print(s)

    min_value = 1e9
    for i in range(n):
        for j in range(i + 1, n):
            for x in range(i + 1, n):
                for y in range(x + 1, n):
                    if i != x and i != y and j != x and j != y:
                        print(i,j, x, y, s[i][j], s[x][y])
                        value = abs(s[i][j] - s[x][y])
                        if min_value > value:
                            min_value = value 

    print(min_value)
    
    