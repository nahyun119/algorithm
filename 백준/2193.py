# 갯수 규칙이 피보나치 수열이랑 비슷,, 

def main():
    n = int(input())

    dp = [0] * (n + 1)
    if n == 1:
        dp[1] = 1
    else:
        dp[1] = 1
        dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n])

if __name__ ==  "__main__":
    main()