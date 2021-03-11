# 규칙이 있다! 
from collections import deque
import sys
import math 
input = sys.stdin.readline

T = int(input())
result = []

for t in range(T):
    x, y = map(int, input().split())
    distance = y - x 
    
    value = int(math.sqrt(distance))
    value2 = value + 1

    if value == 1: # 1, 2, 3:
        result.append(distance)
    elif distance >= value * value2 + 1:
        result.append(value + value2)
    elif distance >= value ** 2 + 1:
        result.append(value * 2)
    else:
        result.append(value * 2 - 1)


for r in result:
    print(r)
