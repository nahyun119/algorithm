# 모든 보석을 나눠준다. 

import sys
import math
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    jewelry = []
    for i in range(m):
        jewelry.append(int(input()))

    start = 0
    end = max(jewelry) + 1

    sum_value = sum(jewelry)

    result = []
    while start <= end:
        mid = (start + end) // 2
        if mid == 0:
            break

        total = 0
        jealous = 0
        for j in jewelry:
            total += math.ceil(j / mid) # 올림해서 나누어 떨어지지 않는 경우까지 고려 

        if total <= n: # n보다 작거나 같으면 안받는 학생이 있더라도 다 나누어줄 수 있다는 의미, 그리고 다 나누어줄 수 있으므로 mid를 줄인다. 
            result.append(mid) 
            end = mid - 1
        else: # 학생들에게 보석을 다 나누어주지 못했으므로 다 나눠줄수 있도록 늘린다. 
            start = mid + 1
    #print(result)
    print(min(result))

if __name__ ==  "__main__":
    main()