import sys
input = sys.stdin.readline

def main():
    n = int(input())
    costs = list(map(int, input().split()))
    budget = int(input())

    costs.sort()

    start = 0 # 최솟값으로 시작을 정했는데, 그렇게하면 안된다. 0원부터 최대값까지 상한액 범위가 되므로!!!!!!!
    end = costs[-1] # 최소랑 최대값을 각각 시작, 끝 값으로 설정

    result = []

    while start <= end:
        mid = (start + end) // 2

        total = 0

        for cost in costs:
            if cost > mid:
                total += mid
            else:
                total += cost
        #print(start, end, mid, total)

        if total == budget:
            result.append(mid)
            break

        if total > budget:
            end = mid - 1
        else:
            result.append(mid)
            start = mid + 1

    print(max(result))

if __name__ ==  "__main__":
    main()