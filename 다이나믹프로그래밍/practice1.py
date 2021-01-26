from collections import deque

# 내 생각엔 이건 dp 가 아니다,,
# 왜이렇게 푼거니 ㅠㅠㅠㅠㅠ 
# 점화식 먼저 구하고 풀자고!!!!! 


def get_col(i, N, road): # i번째 열만 가져오기  -> 사실 0번째 열만 가져오면 된다.. 
    col = []
    for value in range(N):
        col.append(road[value][i])
    return col

def get_index(col, max_value): # 최댓값을 가진 행 인덱스 정보 가져오기 
    row = []
    for index in range(len(col)):
        if col[index] == max_value:
            row.append(index)
    return row 

def calculate():
    N, M = map(int, input().split())

    road = []
    current = deque() # 현재 위치를 담는 배열 
    dx = [-1, 0, 1]
    dy = [1, 1, 1]


    temp = list(map(int, input().split()))

    for i in range(N):
        road.append(temp[(i * M) : (i + 1) * M])
        
    dp = [0] * (M + 1) # dp 테이블 생성

    col = get_col(0, N, road)
    dp[1] = max(col) # 0번째 열 중에서 최댓값 
    row = get_index(col, dp[1])

    for r in row:
        current.append((r, 0)) # 현재 위치 좌표 추가 
    
    for i in range(2, M + 1):
        real_max = -1
        real_cur = []
        while current: # 현재 위치 모두 비교 
            cur_x, cur_y = current.popleft()
            max_val = -1
            max_d = []
            for j in range(3):
                nx = cur_x + dx[j]
                ny = cur_y + dy[j]
                if nx >= 0 and nx < N and ny >= 0 and ny < M:
                    if max_val < road[nx][ny]:
                        max_d = []
                        max_val = road[nx][ny]
                        max_d.append((nx, ny))
                    elif max_val == road[nx][ny]: # 같은 경우도 다음 이동 좌표로 추가 
                        max_d.append((nx, ny))

            if real_max <= max_val:
                real_max = max_val
                real_cur = max_d
        
        dp[i] = dp[i - 1] + real_max

        for cur in real_cur:
            current.append(cur)
        print(dp)

    print(dp[M])

def main():
    T = int(input())
    for i in range(T):
        calculate()
    

if __name__ ==  "__main__":
    main()