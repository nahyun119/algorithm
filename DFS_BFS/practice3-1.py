from collections import deque
import sys
def main():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = []

    temp = []
    #queue = deque()

    for value in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    S, X, Y = map(int, sys.stdin.readline().rstrip().split())

    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                temp.append((graph[i][j], 0, i, j)) # 바이러스인 부분 queue에 추가 

    temp.sort() # 낮은 순이므로 정렬  
    queue = deque(temp) # deque는 정렬할 수 없으므로 리스트로 먼저 입력 받아서 정렬한 후 deque에 추가 

   

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    
    count = 0

    # def add_quque():
    #     for value in range(1, K + 1):
    #         for i in range(N):
    #             for j in range(N):
    #                 if graph[i][j] == value:
    #                     queue.append((i, j))


    while queue:
        virus, s, x, y = queue.popleft()
        #print(graph)
        if s == S:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N: # 범위 안에 있는 경우 
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus # 바이러스 전염 
                    queue.append((graph[nx][ny], s + 1, nx, ny)) # 바이러스랑 시간, 위치를 모두 queue에 저장 

    # while count < S and S != 0:
    #     #add_quque()
    #     while queue:
    #         virus, s, x, y = queue.popleft()
    #         print(x,y)
    #         if s == S:
    #             break
    #         for i in range(4):
    #             nx = x + dx[i]
    #             ny = y + dy[i]
    #             if nx >= 0 and nx < N and ny >= 0 and ny < N: # 범위 안에 있는 경우 
    #                 if graph[nx][ny] == 0:
    #                     graph[nx][ny] = virus # 바이러스 전염 
    #                     queue.append((graph[nx][ny], s + 1 nx, ny))
                       
    #     count += 1
    #     print(count)
    #     print(graph)
    #     is_done = True
    #     for i in range(N):
    #         for j in range(N):
    #             if graph[i][j] == 0:
    #                 is_done = False
    #     if is_done: # 0이 없으면 종료 
    #         break
    
    print(graph[X- 1][Y-1])
                         

if __name__ ==  "__main__":
    main()