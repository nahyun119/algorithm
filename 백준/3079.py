# 시간 기준으로 이진탐색을 수행
# 그 시간안에 각각 심사대가 몇 명을 처리할 수 있는지 구하면 된다.! 
# 해당 처리 가능한 시간 중 최소인 시간을 구하면 된다. 

import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    wait = []
    for i in range(n):
        wait.append(int(input()))

    start = 0
    end = max(wait) * m # 제일 큰 시간 
    #end = 

    result = []

    while start <= end: 
        mid = (start + end) // 2 # 총 걸리는 시간 
        total = 0
        for i in wait:
            total += mid // i 
        #print(mid, start, end, total)
        if total >= m:
            result.append(mid) 
            end = mid - 1
        # if total > n: # 처리할 수 있는 사람이 더 많으면 mid를 줄인다    
        #     result.append(mid)
        #     end = mid - 1
        else: # 처리할 수 있는 사람이 적으면 mid를 늘린다.
            start = mid + 1
    
    print(min(result))
            

            



if __name__ ==  "__main__":
    main()