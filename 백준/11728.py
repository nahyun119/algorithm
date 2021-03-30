# 투포인터 알고리즘
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_start, a_end = 0, n
b_start, b_end = 0, m

temp = []

while a_start < a_end and b_start < b_end:
    if a[a_start] < b[b_start]:
        temp.append(a[a_start])
        # print(a[a_start], end = ' ')
        a_start += 1
    else:
        temp.append(b[b_start])
        # print(b[b_start], end = ' ')
        b_start += 1
    # print(temp)
# print(a_start, a_end, b_start, b_end)
if a_start < a_end:
    temp.extend(a[a_start:])
elif b_start < b_end:
    temp.extend(b[b_start:])

print(*temp)