from collections import deque


def solve():
    n = int(input())
    rooms = []
    for i in range(n):
        rooms.append(list(map(int, input().split())))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()

    for i in range(n):
        for j in range(n):
            q.append((i, j, [(i, j)], rooms[i][j]))
        
    result = [-1] * (n*n + 1) 

    while q:
        x, y, visited, number = q.popleft()
        #print(x, y, visited, number)
        result[number] = len(visited)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if (nx, ny) not in visited and rooms[nx][ny] == rooms[x][y] + 1:
                    #print(x, y, nx, ny)
                    visited.append((nx, ny))
                    q.append((nx, ny, visited, number))
        
    max_value = max(result)
    return result.index(max_value), max_value

def main():
    T = int(input())
    for i in range(T):
        x, y = solve()
        print("#" + str(i + 1), x, y)
if __name__ ==  "__main__":
    main()