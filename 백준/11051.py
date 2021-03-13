# 이항 계수 -> nCk
# -> 팩토리얼을 사용하는데 시간이 오래걸리므로 dp 이용 

n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1
for i in range(k + 1):
    dp[i][i] = 1

for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

print(dp[n][k] % 10007)