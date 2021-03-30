# 너비와 높이에 대해서 각각 투 포인터를 진행해야할거같다. 

import sys
input = sys.stdin.readline 
n, c = map(int, input().split())
stones = {}
x_index = -1
y_index = -1
for i in range(n):
    y, x, value = map(int, input().split())
    if x > x_index:
        x_index = x 
    if y > y_index:
        y_index = y
    stones[(x, y)] = value 

result = -1

h_start = 0
h_end = x_index

result = -1

while h_start < h_end:
    w_start = 0
    w_end = y_index

    while w_start < w_end:
        count = 0 
        value = 0
        for x, y in stones:
            if h_start <= x <= h_end and w_start <= y <= w_end:
                count += 1
                value += stones[(x, y)]
        
        if count <= c: # 늘리면 된다.
            if result < value:
                result = value 

            temp = w_start
            

