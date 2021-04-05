import sys 
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
not_avail = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    not_avail[a].append(b)
    not_avail[b].append(a) 

count = 0 
for i in range(1, n - 1):
    for j in range(i + 1, n):
        if j in not_avail[i]: # 조합 불가능한 상태 
            continue 
        else: # 조합 가능한 상태라면 
            for k in range(j + 1, n + 1):
                if k not in not_avail[i] and k not in not_avail[j]:
                    # print(i, j, k)
                    count += 1
print(count)
