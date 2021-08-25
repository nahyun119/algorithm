import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

dp = [0] * n 

answer = 0 # 경우의 수 

for i, number in enumerate(numbers):
    if i == 0: # 첫번째 원소인 경우
        dp[0] = number 
        if n == 1: # 원소 한 개인 경우
            if m == number:
                answer += 1
    else:
        if numbers[i - 1] + number == m and dp[i - 1] + number != m: # 이전 합인데 누적합이랑 겹칠 수 있으므로!
            answer += 1
            
        # 누적 합 + 현재 숫자
        if dp[i - 1] + number == m: # 누적 합 
            answer += 1
            dp[i] = number
        elif dp[i - 1] + number < m:
            dp[i] = dp[i - 1] + number
        else:
            dp[i] = number # 초기화 
             
        # 현재 숫자 (누적 합 아닌 경우 )
        if number == m:
            answer += 1


print(answer) 


        