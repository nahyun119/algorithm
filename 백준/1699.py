import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    m = int(i ** 0.5)
    #print(m, m* m, i)
    if m * m == i: # 자기자신이 어떤 수의 제곱인 경우   
        dp[i] = 1
    else:
        min_value = 1e9
        for j in range(m, 0, -1):
            if min_value > dp[i - j * j]:
                min_value = dp[i - j * j]
        dp[i] = min(dp[i - 1] + 1, 1 + min_value)

print(dp[n])