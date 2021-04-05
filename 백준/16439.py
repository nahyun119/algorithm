import sys
import itertools
input = sys.stdin.readline
n, m = map(int, input().split())

prefer = []
for i in range(n):
    prefer.append(list(map(int, input().split())))

# 최대 3 종류이므로 1종류를 택할 수도 있다. 
avail = list(itertools.combinations([x for x in range(m)], 3)) # 최대 3종류이므로 
max_value = -1
for i in avail:
    total = 0
    for j in range(n):
        total += max(prefer[j][i[0]], prefer[j][i[1]], prefer[j][i[2]])
    if total > max_value:
        max_value = total 

print(max_value)

