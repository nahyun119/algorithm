import sys
from collections import deque
input = sys.stdin.readline 
n = int(input())

def is_odd(number): # 홀수 구하기 
    s_number = str(number)
    count = 0
    for i in s_number:
        if int(i) % 2 == 1:
            count += 1
    return count 

queue = deque()
queue.append((n, 0)) # 숫자랑 홀수 갯수 

min_value = 1e9
max_value = -1

while queue: # 한 자리수 보다 클 때까지 
    number, value = queue.popleft()
    # print(number, value)
    value += is_odd(number) # 홀수 갯수 구하기
    s_number = str(number)
    length = len(s_number)

    if length == 1: # 한 자리수라면 종료 
        if min_value > value:
            min_value = value 
        if max_value < value:
            max_value = value 
        continue 
    
    elif length == 2: # 두 자리수라면 반으로 나눈다.
        number = int(s_number[0]) + int(s_number[1])
        queue.append((number, value))
    
    elif length >= 3: # 세 자리수 이상이라면 세 자리수로 나눈다. 
        for i in range(1, length - 1):
            for j in range(1, length - i):
                new = int(s_number[:i]) + int(s_number[i: i + j]) + int(s_number[i+j:])
                queue.append((new, value))

print(min_value, max_value)

