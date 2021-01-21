# 조건에 해당하는 최소, 최대 등 가장 적절한 값을 찾는 경우,
# 그 값을 찾는다는 느낌으로 이진 탐색을 한다.
# 그 전에 구하려는 값의 범위를 조건을 통해 먼저 알고 
# 그 범위 안에서 이진 탐색을 통해(조건에 맞게 start, end를 조정하면서) 적절한 값을 찾으면 된다. 

def main():
    N, M = map(int, input().split())

    foods = list(map(int, input().split()))

    foods.sort()

    start = 0
    end = max(foods)

    result = 0
    # 이진 탐색의 대상이 foods가 아니라 자르려고 하는 높이로 하면 된다. 
    # 최소 0부터 떡의 최대 길이까지 자르려고 하는 높이의 범위가 된다. 
    while start <= end:
        total = 0
        mid = (start + end ) // 2

        for value in foods:
            if value > mid:
                total += value - mid

        # 떡의 양이 부족한 경우, 끝을 줄이기 
        if total < M:
            end = mid - 1
        # 떡의 양이 큰 경우, 시작점을 줄이기 자를 수 있는 최대 높이 이므로 
        if total >= M:
            result = mid
            start = mid + 1

    print(result)  

if __name__ ==  "__main__":
    main() 