def solve(n):
    graph = list(map(int, input().split()))
    
    edges = [[] for i in range(100)]
    for i in range(0, n * 2, 2):
        edges[graph[i]].append(graph[i + 1])

    visited = [0] * 100
    
    result = []
    def dfs(node, visited):
        #print(node)
        visited[node] = 1

        if node == 99:
            result.append(True)
            return 

        for i in edges[node]:
            if visited[i] == 0:
                dfs(i, visited)
        
    
    dfs(0, visited)
    
    if result:
        return 1
    else:
        return 0

def main():
    for _ in range(1):
        a, b = map(int, input().split())
        result = solve(b)
        print("#" + str(a), result)

if __name__ ==  "__main__":
    main()