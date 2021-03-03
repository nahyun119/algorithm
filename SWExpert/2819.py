import copy

def solve():
    graph = []
    for i in range(4):
        graph.append(list(map(int, input().split())))
    
    result = set()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, step, v):
        
        if step >= 6:
            result.add(v)
            return 

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
                dfs(nx, ny, step + 1, v + str(graph[nx][ny]))

    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, str(graph[i][j]))
    
    return len(result)
    
    

def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()