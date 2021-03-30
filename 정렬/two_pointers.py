# 특정한 합을 가지는 부분 연속 수열에 대해서 적용가능한 알고리즘
# 완전 탐색으로 진행할 때 시간 초과가 발생할 때, 이 알고리즘을 사용하면  O(n) 시간 안에 해결 가능 
numbers = list(map(int, input().split()))
m = int(input())
start = 0
end = 0

n = len(numbers)

count = 0
interval_sum = 0

for start in range(n):
    while interval_sum < m and end < n: # 부분 합이 m 이상이거나 end = n인 경우 start ++이므로 
        interval_sum += numbers[end]
        end += 1
    
    if interval_sum == m: # 부분합이 m이라면 증가 
        count += 1

    # 시작 부분이 증가하므로 현재 시작 부분 값을 뺀다. 
    interval_sum -= numbers[start]

print(count)

