# 다시 풀어봐야 하는 문제
# 파라메트릭 서치 문제 

def main():
    N, C = map(int, input().split())
    houses = []
    for i in range(N):
        houses.append(int(input()))

    houses.sort()

    min_d = houses[1] - houses[0] #왜,,? 더 작은 값이 있을 수 있자뉴아 ,, 
    max_d = houses[N - 1] - houses[0]

    result = 0

    while min_d <= max_d:
        mid = (min_d + max_d) // 2
        count = 1
        first = houses[0]

        for i in range(1, n): # 앞에서부터 설치 
            if houses[i] >= mid + value:
                value = houses[i]
                count += 1
        if count >= C:
            min_d = mid + 1
            result = mid 
        else:
            max_d = mid - 1

if __name__ ==  "__main__":
    main() 