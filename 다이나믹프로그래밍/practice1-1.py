# 점화식 
# dp[i][j] = road[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

result = []

def calculate():
    global result 
    N, M = map(int, input().split())

    road = []
    
    dx = [-1, 0, 1]
    dy = [1, 1, 1]


    temp = list(map(int, input().split()))

    for i in range(N):
        road.append(temp[(i * M) : (i + 1) * M])
        
    for j in range(1, M):
        for i in range(N):
            if i == 0: # 왼쪽 위인 경우 
                up = 0
            else:
                up = road[i - 1][j - 1]
            if i == N - 1: # 왼쪽 맨 아래인 경우 
                down = 0
            else:
                down = road[i + 1][j - 1]

            left = road[i][j - 1]
            road[i][j] = road[i][j] + max(up, down, left)
    
    max_result = -1
    
    for i in range(N):
        max_result = max(max_result, road[i][M - 1])

    result.append(max_result)
    


def main():
    global result
    T = int(input())

    for i in range(T):
        calculate()
    
    for i in range(T):
        print(result[i])
    

if __name__ ==  "__main__":
    main()