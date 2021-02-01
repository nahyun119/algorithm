# 한 컴퓨터에 바이러스가 걸리면 이어진 순서대로 계속 바이러스가 걸리므로
# 모든 컴퓨터를 다 탐색할 필요 없어서 
# dfs 이용

def main():
    n = int(input()) # 컴퓨터 수 
    m = int(input()) # 연결 수 
     
    graph = [[0] * (n + 1) for _ in range(n + 1)] # 1~n번까지이므로 

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1 # 양방향 

    visited = [0] * (n + 1)
    #visited[1] = 1 # 1번부터 시작

    result = []

    def dfs(start, visited):
        visited[start] = 1
        result.append(start)
        for i in range(1, n + 1):
            if graph[start][i] == 1 and visited[i] == 0:
                dfs(i, visited)
    
    dfs(1, visited)
    #print(result)
    print(len(result) - 1) # 1번 컴퓨터 제외 

if __name__ ==  "__main__":
    main()