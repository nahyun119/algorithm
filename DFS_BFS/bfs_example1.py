from collections import deque

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        node = queue.popleft()
        print(node)
        for value in graph[node]:
            if visited[value] == 0:
                queue.append(value)
                visited[value] = 1


def main():
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]
    visited = [0] * 9

    bfs(graph, 1, visited)

if __name__ ==  "__main__":
    main()