import sys
input = sys.stdin.readline

def rotate(d):
    if d == 0:
        d = 3
    else:
        d -= 1
    return d

def get_back(d):
    if d == 0 or d == 1:
        d += 2
    else:
        d -= 2
    return d 


def main():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())

    dx = [-1, 0, 1, 0] # 북 동 남 서 전진 
    dy = [0, 1, 0, -1]

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    count = 0
    while True:
        #print(r, c, d)
        if graph[r][c] == 0: # 현재 위치가 빈 칸이라면 
            graph[r][c] = 2 # 청소한 곳은 2로 표시 
            count += 1
        
        for i in range(4):
            current_d = rotate(d)
            nx = r + dx[current_d]
            ny = c + dy[current_d]
            is_ok = False
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 0:
                    r = nx
                    c = ny
                    d = current_d
                    is_ok = True
                    break 
            d = current_d

        if not is_ok: # 네 방향 모두 벽이거나 청소가 된 경우 0이 없는 경우
            back_d = get_back(d)
            r = r + dx[back_d]
            c = c + dy[back_d]
            if graph[r][c] == 1: # 벽이라 이동할 수 없는 경우 
                break 
        
    print(count)

        





if __name__ ==  "__main__":
    main()