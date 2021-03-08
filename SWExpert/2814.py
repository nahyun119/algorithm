t = int(input())

def dfs(x, value):
    global max_value
    value += 1
    max_value = max(max_value, value)
    #print(max_value)
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i, value)

    visited[x] = 0
            

for i in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0 for _ in range(n + 1)]
    max_value = 0

    for j in range(n):
        dfs(j, 0)

    print("#" + str(i + 1), max_value)


        