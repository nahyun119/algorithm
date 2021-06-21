import sys 
input = sys.stdin.readline 

A = input().strip()
B = input().strip()

a = len(A)
b = len(B)

dp = [[0] * a for _ in range(b)] # 행은 B 문자열 길이만큼, 열은 A 문자열 길이만큼 

for i in range(a): # 0번째 행 초기화
    if A[i] == B[0]:
        dp[0][i] = 1
        for j in range(i, a): 
            dp[0][j] = 1 # 1개라도 겹치면 최소 1개 같은거이므로 1로 초기화
        break 

for i in range(b): # 0번째 열 초기화 
    if A[0] == B[i]:
        dp[i][0] = 1
        for j in range(i, b):
            dp[j][0] = 1
        break 

for i in range(1, b):
    for j in range(1, a):
        count = 0
        if B[i] == A[j]:
            count = 1 # 같은 경우 이전 열, 행에 대해서 + 1 해준다! max해서 모든 경우에서 하면 겹치는 경우가 생긴다
        dp[i][j] = max(dp[i - 1][j - 1] + count * 1 , dp[i - 1][j], dp[i][j - 1])
        
# print(dp)
print(dp[b - 1][a - 1])