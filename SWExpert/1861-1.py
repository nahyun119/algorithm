# 단순 bfs 로 풀면 시간초과 발생 
# dp 같다 예를들어서 n = 3인 경우 9는 자기자신만, 그리고 9에서 8로 갈 수 있는 경우 1 + 1해서 2개 이렇게 

def solve():
    n = int(input())

    rooms = [[] for _ in range(n * n + 1)]

    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            rooms[temp[j]] = (i, j)
            
    #print(rooms)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dp = [1] * (n * n + 1)

    for i in range(n * n, 1, -1): # 제일 높은 숫자부터 2까지 
        x, y = rooms[i]
        nx, ny = rooms[i - 1]
        #print(i, dp)
        for j in range(4):
            cx = x + dx[j]
            cy = y + dy[j]
            #print(x, y, nx, ny, cx, cy)
            if cx >= 0 and cx < n and cy >= 0 and cy < n:
                if cx == nx and cy == ny:
                    #print(i, i - 1, dp)
                    dp[i - 1] = dp[i] + 1
                    break 

    max_value = max(dp)

    answer = [dp.index(max_value), max_value]
    return answer 
    

def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), *result)
if __name__ ==  "__main__":
    main()