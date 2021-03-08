from collections import deque
def solve():
    maze = []

    for i in range(100):
        temp = list(input().strip())
        for j in range(100):
            if temp[j] == '2':
                start = (i, j)
            if temp[j] == '3':
                end = (i, j)
        maze.append(temp)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append(start)
    visited = [[0] * 100 for _ in range(100)]
    visited[start[0]][start[1]] = 1

    while q:
        x, y = q.popleft()

        if x == end[0] and y == end[1]:
            return 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < 100 and ny >= 0 and ny < 100:
                if visited[nx][ny] == 0 and maze[nx][ny] != '1' :
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    
    return 0



def main():
    for i in range(1):
        n = int(input())
        result = solve()
        print("#" + str(n), result)

if __name__ ==  "__main__":
    main()