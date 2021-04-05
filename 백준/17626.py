# 브루트 포스로 이용할 수 있지만 
# dp로 풀 수 있을 것 같다.

n = int(input())
dp = [1e9] * (n + 1)

for i in range(1, n + 1):
    if i * i <= n:
        dp[i * i] = 1

for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + dp[j * j])

print(dp[n])