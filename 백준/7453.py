# 이중 포문 돌리고
# 나머지 2개는 투 포인터 이용 

import sys
input = sys.stdin.readline 

n = int(input())
A = []
B = []
C = []
D = []

for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

start = []
end = {}

for i in range(n):
    for j in range(n):
        start.append(A[i] + B[j]) # a, b 합 구하기 
        # print(end.get(C[i] + D[j], 0))
        end[C[i] + D[j]] = end.get(C[i] + D[j], 0) + 1 # c, d 합 구하기 
        # print(start, end)
count = 0
for value in start:
    count += end.get(-value, 0) # 만약 c,d 합 중에서 a,b의 반대값이 있다면 

print(count)
            