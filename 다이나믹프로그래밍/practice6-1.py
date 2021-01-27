# dp 를 이용한 경우
# 두 문자열을 비교한 것이므로 이차원 배열을 만든다.

def main():
    A = str(input())
    B = str(input())

    a = len(A)
    b = len(B)

    dp = [[0] * (b + 1) for _ in range(a + 1)]

    for i in range(1, a + 1):
        dp[i][0] = i

    for i in range(1, b + 1):
        dp[0][i] = i
    
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if A[i - 1] != B[j - 1]: # 두 문자가 다른 경우 
                dp[i][j] = 1 + min(dp[i -1][j -1], dp[i][j - 1], dp[i - 1][j])
            else: # 두 문자가 같은 경우 
                dp[i][j] = dp[i - 1][j - 1]



    print(dp[a][b])

if __name__ ==  "__main__":
    main()