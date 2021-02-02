import sys
import math
input = sys.stdin.readline

# 계속 틀렸다고 나와서 뭐가 문제인가 싶었는데,,
# 승률을 구하는 작업에서 (y / x) * 100 이렇게하니까 제대로 값이 나오지 않았다.  ex) 50 29 면 58이 되어야하는데 57이 나옴
# 그래서 (y * 100) / x 로 해서 진행했더니 통과했다. 

def main():
    x, y = map(int, input().split())
    z = int((y * 100) / x) 
    #print((y / x), (y / x) * 100, )
    start = 0
    end = x
    #print(z)
    result = []
    
    while start <= end:
        mid = (start + end) // 2

        nx = x + mid
        ny = y + mid 
        nz = int((ny * 100) / nx)
        #print(nx, ny, nz, mid)

        if nz <= z: # 같거나 작으면 더 큰 범위로 이동 
            start = mid + 1
        else: # 크면 큰 값을 만든 mid 값을 결과 리스트에 추가 
            result.append(mid)
            end = mid - 1

    #print(result)
    if result:
        print(min(result)) # 제일 작은 값이므로 최솟값 
    else: 
        print(-1) # result가 빈 경우, 변하지 않는다는 의미이므로
    #print(mid)

if __name__ ==  "__main__":
    main()