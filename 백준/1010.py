result = []
def solve():
    global result 
    n, m = map(int, input().split())

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
    
    for i in range(n):
        for j in range(i + 1, m):
            if i == 0:
                dp[i][j] = j + 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
    #print(dp)
    #print(dp[n- 1][m - 1])
    result.append(dp[n- 1][m - 1])



def main():
    global result
    n = int(input())
    for i in range(n):
        solve()
    for re in result:
        print(re)


if __name__ ==  "__main__":
    main()