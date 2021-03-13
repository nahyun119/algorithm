# dfs로 풀었는데 반례도 다 맞는데,,, 흠,,
# knapsack 알고리즘을 사용해보자 

n, k = map(int, input().split())
bags = []
for i in range(n):
    w, v = map(int, input().split())
    bags.append((w, v))

max_value = 0
visited = [0] * n

def dfs(index, weight, value, visited):
    global max_value
    visited[index] = 1
    if weight <= k:
        if max_value < value:
            max_value = value 
    else:
        return 
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, weight + bags[i][0], value + bags[i][1], visited)

    visited[index] = 0

for i in range(n):
    dfs(i, bags[i][0], bags[i][1], visited)

print(max_value)