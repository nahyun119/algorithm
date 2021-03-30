import sys
input = sys.stdin.readline 

# 길이 n짜리 수열의 부분합 -> 투 포인터 알고리즘
n, s = map(int, input().split())
numbers = list(map(int, input().split()))

end = 0
interval_sum = 0
result = 1e9

for i in range(n):
    while interval_sum < s and end < n: # 부분합이 s보다 작고 end < n인 경우 end + 1
        interval_sum += numbers[end]
        end += 1
    if interval_sum >= s: # 부분 합이상이라면 
        r = (end - 1 - i) + 1
        # print(i, end - 1, interval_sum)
        if result > r:
            result = r 
    # start 땡기므로 빼야한다. 
    interval_sum -= numbers[i]

if result >= 1e9: # 합을 못 만드는 경우 0을 출력 
    print(0)
else:
    print(result)
        
