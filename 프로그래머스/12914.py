def solution(n):
    answer = 0
    
    dp = [0] * (n + 2)
    
    dp[1] = 1
    dp[2] = 2
    
    if n >= 3:
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
    answer = dp[n] % 1234567 # 나누기 잊지말아!!!
    
    return answer