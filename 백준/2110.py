import sys

input = sys.stdin.readline

def main():
    n, c = map(int, input().split())
    houses = []

    for i in range(n):
        a = int(input())
        houses.append(a)

    houses.sort()
    start = 1 # 1이상부터 시작하므로
    end = houses[-1] - houses[0] # 최솟값과 최댓값 차이만큼 거리를 둘 수 있다.

    result = 0
    while start <= end:
        mid = (start + end) // 2
        #print(start, end, mid)
        is_ok = False
        count = 1
        house = houses[0] # 맨 처음에 설치하는 최적해가 항상 존재하기 때문이다. 
        for j in range(1, n):
            if houses[j] >= house + mid:
                count += 1
                house = houses[j]
        if count >= c: # 하나라도 만들 수 있는 경우 더 큰 수로 탐색하기 위해 오른쪽으로 이동. 
            start = mid + 1
            result = mid
            is_ok = True
                   
        if not is_ok: # 하나라도 만들 수 없는 경우 더 작은 수로 탐색하기 위해 왼쪽으로 이동. 
            end = mid - 1

    print(result)     
            

if __name__ ==  "__main__":
    main()