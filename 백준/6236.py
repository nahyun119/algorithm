import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    budget = []
    for i in range(n):
        budget.append(int(input()))

    total = sum(budget)

    start = 0
    end = 10000 * n # 하루에 쓸 금액이 최대 10000원이므로 

    result = []
    max_value = max(budget)

    while start <= end:
        mid = (start + end) // 2 
        if mid < max_value: # 적어도 사용하는 금액보다는 커야함 
            start = mid + 1
            continue
        count = 1
        remain = mid - budget[0]
        
        for i in range(1, n):
            cost = budget[i]
            if remain >= cost: # 첫번째 날 사용하고 남은 돈이 더 많다. 
                remain -= cost 
            else: # 적으면 다시 인출 
                count += 1
                remain = mid - cost

        #print(count)

        if m >= count: # 그러면 k를 줄이기
            result.append(mid)
            end = mid - 1
        else:
            start = mid + 1
            
    #print(result)
    print(min(result))



if __name__ ==  "__main__":
    main()