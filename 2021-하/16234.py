import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, l, r = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 인접한 나라를 이동을 위해서
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def change(nations, people): # 인구 수 업데이트 
    count = len(nations) # 연합하는 국가 수 
    new_people = people // count 

    for x, y in nations:
        graph[x][y] = new_people # 새로운 인구 수로 업데이트 

def move(): # 인구 이동 
    flag = False # 인구이동을 진행했는지 

    visited = [[0] * n for _ in range(n)] # 이동할 때마다 새로운 방문


    def dfs(x, y):
        global n, l, r
        visited[x][y] = 1

        nations = [(x, y)]
        people = graph[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 : # 방문 안한 상태
                    if l <= abs(graph[x][y] - graph[nx][ny]) <= r: # 국경선 열기위한 조건 
                        na, p = dfs(nx, ny)
                        nations.extend(na)
                        # print(nations, people)
                        people += p

        return nations, people

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0: # 방문하지 않은 곳이라면
                nations, people = dfs(i, j)
                if len(nations) > 1: # 자기 자신만 있는 경우 인구 이동을 할 필요 없음, 1이상이면 인구이동을 진행한다.  
                    flag = True
                    # print(nations, people)
                    # 어차피 dfs 한번에 연합할 수 있는 모든 곳을 방문하므로 끝나면 인구 이동 진행
                    change(nations, people) # 인구 업데이트 

    return flag                 





result = 0
flag = True 

while flag:
    flag = move()
    if flag: 
        result += 1
    # print(result)
    # print("================")
    # print(graph)
    # print()
    # print()

print(result)