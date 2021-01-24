def main():
    N = int(input())

    dp = [[0] * N for i in range(2)] # dp 테이블 만들기

    dp[0][0] = 1

    for i in range(2): # 세로 이동 
        for j in range(N): # 가로 이동 
            print(dp)
            if i < 2 and j + 1 < N: # 1 * 2 놓는 경우 
                #print(i, j)
                dp[i][j] += 1
                dp[i][j + 1] += 1
            if i + 1 < 2 and j < N: # 2 * 1 놓는 경우
                #print(i, j)
                dp[i][j] += 1
                dp[i + 1][j] += 1
            if i + 1 < 2 and j + 1 < N: # 2 * 2 놓는 경우
                #print(i, j)
                dp[i][j] += 1
                dp[i + 1][j] += 1
                dp[i][j + 1] += 1
                dp[i + 1][j + 1] += 1
    
    print(dp)


                

    
    

if __name__ ==  "__main__":
    main()