import sys
input = sys.stdin.readline 
n = int(input())
numbers = list(map(int, input().split()))

start = 0
end = n - 1
numbers.sort()

result = abs(numbers[start] + numbers[end])
f_start = start
f_end = end

while start < end:
    temp = numbers[start] + numbers[end]
    if abs(temp) < result:
        result = abs(temp)
        f_start = start
        f_end = end 
        if result == 0: # 0이면 더 이상 탐색할 필요 없음 
            break 
    if temp < 0: # 음수라면 
        start += 1 # 값의 범위를 줄여야하므로 오른쪽으로 이동 
    else:
        end -= 1 # 값의 범위를 줄여야 하므로 왼쪽으로 이동 

print(numbers[f_start], numbers[f_end])