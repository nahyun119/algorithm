n  = int(input())
numbers = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = numbers[i]
    #print(dp)
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[j] + numbers[i], dp[i])

print(max(dp))