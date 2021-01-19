# 시간 초과의 늪에 빠져있었다.. 
# 다음에 한번 더 시간 줄일 수 있는 방법 찾아보기 
from collections import deque

def main():
    N, L, R = map(int, input().split())

    country = []
    for value in range(N):
        country.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    count = 0

    
    while True:
        not_move_count = 0

        union = [[-1] * N for _ in range(N)]
        nations = []

        for i in range(N): # 나라를 모두 살펴서 연합을 만든 후에 그 다음에 인구이동 연합 만들고 바로 인구 이동하지 않는다. 
            for j in range(N):
                if union[i][j] == -1:
                    queue = deque()
                    visited = []
                    
                    queue.append((i, j))
                    visited.append((i, j))
                    union[i][j] = count
                    country_p = country[i][j] # 인구 수 
                    country_n = 1
                        
                    while queue: # queue 가 비워지면 인구 이동 연합 모두 탐색 완료 
                        x, y = queue.popleft()

                        for value in range(4):
                            nx = x + dx[value]
                            ny = y + dy[value]
                            if nx >= 0 and nx < N and ny >= 0 and ny < N and union[nx][ny] == -1: # 범위 안에 있는 경우 
                                diff = abs(country[x][y] - country[nx][ny])
                                if diff >= L and diff <= R and (nx, ny) not in visited:
                                    queue.append((nx, ny))
                                    visited.append((nx, ny))
                                    country_p += country[nx][ny]
                                    union[nx][ny] = count
                                    country_n += 1
                    
                    #country_n = len(visited) # 연합 국가 수 

                    if country_n == 1: # 자기 자신 밖에 없다는 의미이므로 인구 이동할 필요 없다. 
                        not_move_count += 1
                        continue

                    else:
                        new_p = country_p // country_n # 새로운 인구 수 
                        nations.append((visited, new_p))
                        country_n = 0

        for nation, new_p in nations:
            for x, y in nation:
                country[x][y] = new_p
    
        if not_move_count == N * N:
            break
        count += 1

    print(count)        

        


if __name__ ==  "__main__":
    main()