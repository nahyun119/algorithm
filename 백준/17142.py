import sys
from collections import deque
import itertools
import copy
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(graph, n): # 0이 있는지 확인 
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 0:
                return False
    return True

def bfs(v, g, virus, n):
    global dx, dy
    result = []
    gr = copy.deepcopy(g)


    q = deque()
    visited = [[0] * n for _ in range(n)]
    for x in v: # 후보군 모두를 다 넣는다. -> 이게 중요!!! 이걸 몰라서 헤맸다ㅠㅠ 
        q.append((virus[x][0], virus[x][1], 0))
    last_dist = 0
    while q:
        cx, cy, c = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if visited[nx][ny] == 0 and gr[nx][ny] != 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny, c + 1))
                    if gr[nx][ny] == 0: # 최대 걸린 시간 
                        gr[nx][ny] = 2
                        last_dist = c + 1

    if check(gr, n):
        return last_dist
    else:
        return -1 
    

def main():
    n , m = map(int, input().split())
    graph = []
    virus = []

    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            if temp[j] == 2:
                virus.append((i, j))
        graph.append(temp)

    com_virus = list(itertools.combinations([x for x in range(len(virus))], m))
    
    result = []

    for c in com_virus:
        #print(graph)
        r = bfs(c, graph, virus, n)
        result.append(r)

    if sum(result) == -1 * len(com_virus):
        print(-1)
    else:
        print(min([x for x in result if x != -1]))

    #print(result)

    


if __name__ ==  "__main__":
    main()