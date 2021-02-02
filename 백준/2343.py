import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    lessons = list(map(int, input().split()))

    start = 0
    end = sum(lessons)

    #lessons.sort()

    result = []
    while start <= end:
        mid = (start + end) // 2
        total = 0
        count = 1
        is_over = False
        for lesson in lessons:
            if lesson > mid: # 블루레이 크기가 최소 레슨 길이보다는 커야하므로 
                is_over = True
                break 
            if count > m: # 블루레이 갯수가 주어진 것보다 많은 경우도 안됨. 
                is_over = True
            total += lesson
            if total > mid:
                if count < m:  # 새 블루레이에 담을 수 있도록 
                    total = lesson 
                    count += 1 
                else:
                    is_over = True # 해당 크기로 블루레이 안에 순서대로 담을 수 없다 
            elif total == mid: # 크기만큼 찬 경우 새 블루레이로 이동할 수 있도록 
                count += 1
                total = 0
        #print(start, end, mid, is_over)
        if not is_over:
            result.append(mid)
            end = mid - 1 # 블루레이 안에 담을 수 있으므로 블루레이 길이를 줄임 
        else: # 블루레이 안에 담을 수 없으므로 블루레이 길이를 늘림 
            start = mid + 1

    #print(result)
    print(min(result))

if __name__ ==  "__main__":
    main()