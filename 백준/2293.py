# 사용한 동전 구성이 같은데 순서가 달라도 같은 경우 
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

dp = [0] * (k + 1)
dp[0] = 1
for c in coin: # 각 코인을 사용해서 만들 수 있는 경우의수를 계산 
    for j in range(1, k + 1):
        if j - c >= 0:
            dp[j] += dp[j - c]

print(dp[k])
