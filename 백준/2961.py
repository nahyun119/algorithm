# 비트 연산을 이용해보자
import sys 
input = sys.stdin.readline 

n = int(input())
taste = []
for i in range(n):
    s, b = map(int, input().split())
    taste.append((s, b))

min_value = 1e9 

for i in range(1, (1 << n)):
    s_taste = 1
    b_taste = 0
    for j in range(n):
        if i & (1 << j) != 0:
            s, b = taste[j]
            s_taste *= s 
            b_taste += b 
    diff = abs(s_taste - b_taste)
    # print(s_taste, b_taste)
    if diff < min_value:
        min_value = diff 

print(min_value)