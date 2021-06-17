import sys 
input = sys.stdin.readline 
number = int(input())
dp = [1e9 for i in range(5001)]

dp[3] = 1
dp[5] = 1 # 초기화

if number < 6:
    if dp[number] >= 1e9:
        print(-1)
    else:
        print(dp[number]) # 3~5같은 경우는 안해도 알 수 있다. 
else:
    for i in range(6, number + 1):
        dp[i] = min(dp[3] + dp[i - 3], dp[5] + dp[i - 5])
    if dp[number] >= 1e9:
        print(-1)
    else:
        print(dp[number])