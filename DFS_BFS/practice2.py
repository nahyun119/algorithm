# 이것도 시간초과가 났는데, 이전처럼 입력때문인가해서
# import sys하고 입력 값을 받는 방법을 변경하였다.
# 그리고 pypy3이 있다면 얘가 더 성능?이 좋아서 빨리 처리된다고 해서 
# python3이 아니라 pypy3으로 했더니 통과함 


import sys

result = 0

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    #graph = [[0] for _ in range(N)] # 초기 맵 리스트
    temp = [[0] * M for _ in range(N)] # 벽을 설치한 후 맵 리스트
    graph = []
    for value in range(N):
        # graph[value] = list(map(int, input().split()))
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def get_result(): # 0 갯수 구하는 함수 
        score = 0
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 0:
                    score += 1
        return score

    def virus(x, y): # 바이러스 퍼지도록
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    #print(temp)
                    virus(nx, ny)

    def dfs(count):
        global result
        if count == 3:
            for i in range(N):
                for j in range(M):
                    temp[i][j] = graph[i][j]

            for i in range(N):
                for j in range(M):
                    if temp[i][j] == 2:
                        virus(i, j)
            #print(temp)
            #print(result, get_result())
            result = max(result, get_result())
            return 

        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    count += 1
                    dfs(count)
                    #print(result)
                    graph[i][j] = 0
                    count -= 1
    

    dfs(0)
    print(result)



if __name__ ==  "__main__":
    main()