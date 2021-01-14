# 이동하는 경우에 이동한 칸의 수를 += 1 해서 
# 값을 구히도록 했는데
# 그래프에 해당 칸으로 갈 때까지 지나는 칸 수를 구해서 저장할 수도 있다. -> example2-1.py

from collections import deque

def main():
    N, M = map(int, input().split())

    graph = []
    for value in range(N):
        graph.append(list(map(int, input())))
    
    queue = deque()
    #visited = [[0] * M for _ in range(N)]

    queue.append((0,0))

    result = 0

    while queue:
        node = queue.popleft()
        # 갔다왔으므로 0으로 표시 
        graph[node[0]][node[1]] = 0
        result += 1
        if node[0] == N - 1 and node[1] == M - 1:
            print(result)
            return 
        if node[0] < N - 1 and graph[node[0] + 1][node[1]] == 1:
            queue.append((node[0] + 1,  node[1]))
        if node[1] < M - 1 and graph[node[0]][node[1] + 1] == 1:
            queue.append((node[0], node[1]+ 1))

    



if __name__ ==  "__main__":
    main()
