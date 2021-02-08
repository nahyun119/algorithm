# 그래프 탐색인데 뭔가 bfs, dfs 같다 그게 그거지만,, 


import sys
input = sys.stdin.readline

def main():
    sys.setrecursionlimit(10 ** 7)
    n, m  = map(int, input().split())
    graph = [[] for _ in range(n + 1)] # 1부터 시작 
    
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (n + 1)

    def dfs(node, graph, visited):
        #print(node)
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                dfs(i, graph, visited)

    count = 0 
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i, graph, visited)
            count += 1
    
    print(count)



if __name__ ==  "__main__":
    main()