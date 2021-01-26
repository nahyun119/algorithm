def main():
    N = int(input())

    triangle = []
    for i in range(N):
        triangle.append(list(map(int, input().split())))
    
    triangle.reverse()
    
    for i in range(1, N):
        for j in range(N - i):
            # if j == 0:
            #     left = 0
            # else:
            #     left = triangle[i - 1][j + 1]
            # if j == (N - i - 1):
            #     right = 0
            # else:
            #     right = triangle[i - 1][j]
            
           triangle[i][j] = triangle[i][j] + max(triangle[i - 1][j], triangle[i - 1][j + 1])

    print(triangle[N - 1][0])


if __name__ ==  "__main__":
    main()