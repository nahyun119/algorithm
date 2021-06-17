import sys
input = sys.stdin.readline
n = int(input())

time = []
profit = []
time.append(0) # 1~n 맞추려고 
profit.append(0)

for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

dp = [0 for i in range(n + 1)] # 배열 생성

for i in range(1, n + 1):
    if i + time[i] <= n : # 이하에 가능한 경우 
        max_value = max(dp)
        if max_value < dp[i] + profit[i]:
            dp[i] = dp[i] + profit[i]
            if i + time[i] < n + 1:
                dp[i + time[i]] = dp[i] # 다음날 데이터도 최댓값으로 업데이트 
        else:
            dp[i] = profit[i]

    print(i, dp)
print(max(dp))