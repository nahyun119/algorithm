from collections import deque

def solve():
    maze = []

    for i in range(16):
        temp = list(input().strip())
        if '2' in temp:
            start = (i, temp.index('2'))
        maze.append(temp)

    q = deque()
    q.append(start)

    visited = [[0] * 16 for _ in range(16)]
    visited[start[0]][start[1]] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(start)
    while q:
        x, y = q.popleft()
        #print(x, y)
        if maze[x][y] == '3':
            return 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < 16 and ny >= 0 and ny < 16:
                if maze[nx][ny] != '1' and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
            
    return 0
    

def main():
    for _ in range(1):
        t = int(input())
        result = solve()
        print("#" + str(t), result)

if __name__ ==  "__main__":
    main()