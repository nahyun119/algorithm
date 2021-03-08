import heapq

def solve():
    n = int(input())
    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, visited):
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if visited[nx][ny] == 0 and matrix[nx][ny] != 0:
                    step.append((nx, ny))
                    dfs(nx, ny, visited)

    visited = [[0] * n for _ in range(n)]

    result = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and matrix[i][j] != 0:
                step = [(i, j)]
                dfs(i, j, visited)
                step.sort(key = lambda x : (-x[0], -x[1]))
                x = step[0][0]
                y = step[0][1]
                row = abs(i - x) + 1
                col = abs(j - y) + 1
                # result.append((row * col, row, col))
                heapq.heappush(result, (row * col, row, col))


    # result.sort(key = lambda x : (x[0], x[1]))
    answer = [len(result)]
    while result:
        size, x, y = heapq.heappop(result)
        answer.append(x)
        answer.append(y)

    
    return answer 
    

  


def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), *result)

if __name__ ==  "__main__":
    main()
