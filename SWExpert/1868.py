from collections import deque
import heapq


def solve():
    # sys.setrecursionlimit(10**7)
    n = int(input())
    road = []

    safe = []

    for i in range(n):
        temp = list(input().strip())
        for j in range(n):
            if temp[j] == '.':
                safe.append((i, j))
        road.append(temp)

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    def check(x, y):
        total = 0
        count = 0

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                count += 1
                if road[nx][ny] == '*':
                    total += 1
        if total == 0:
            return count 
        else:
            return -1          

    def bump(x, y, n):

        visited = [[0] * n for _ in range(n)]
        q = deque()
        q.append((x, y))
        visited[x][y] = 1

        while q:
            #print(q)
            cx, cy = q.popleft()
            #print(cx, cy, q)

            total = 0
            queue = []

            for i in range(8):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    #print(nx, ny)
                    if road[nx][ny] == '*':
                        total += 1
                    elif road[nx][ny] != '*' and visited[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1

            if total == 0:
                road[cx][cy] = 0
                for qx, qy in queue:
                    #print(qx, qy)
                    road[qx][qy] = 0
                    q.append((qx, qy))
            else:
                road[cx][cy] = total 

    count = 0
    order = []

    for sx, sy in safe:
        value = check(sx, sy)
        if value != -1:
            heapq.heappush(order, (-value, sx, sy))
        else:
            heapq.heappush(order, (0, sx, sy))



    while order:
        v, x, y = heapq.heappop(order)
        #print(v, x, y)
        if road[x][y] == '.':
            #print(road, count)
            bump(x, y, n)
            count += 1

    #print(road)
    #print(count)
    return count 


def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()