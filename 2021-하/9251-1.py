import sys 
input = sys.stdin.readline 

A = ' ' + input().strip()
B = ' ' + input().strip()

a = len(A)
b = len(B)

dp = [[0] * a for _ in range(b)] # 행은 B 문자열 길이만큼, 열은 A 문자열 길이만큼 

for i in range(1, b):
    for j in range(1, a):
        if B[i] == A[j]:
            # 같은 경우 이전 열, 행에 대해서 + 1 해준다! max해서 모든 경우에서 하면 겹치는 경우가 생긴다
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
print(dp)
print(dp[b - 1][a - 1])