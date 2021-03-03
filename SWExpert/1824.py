# ?에 대해서 모든 경우를 확인해야한다.
# 69개 테스트 케이스 중에서 왜!!!!!!!!!!!!!!! 1개만 틀리냐고!!!!!!!!!! -> 69번 하나 틀린다.. 


from collections import deque
def solve():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(input().strip()))

    memory = '0' # 메모리
    x = 0 
    y = 0
    direc = 0 # 0 : 오른쪽, 1 : 왼쪽, 2 : 위쪽, 3: 아래쪽 

    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1


    def get_next(x, y, direc):
        if direc == 0: # 오른쪽 이동
            if y >= m - 1: # 바깥으로 이동하는 경우 
                y = 0
            else:
                y += 1
        elif direc == 1: # 왼쪽 이동 
            if y <= 0:
                y = m - 1
            else:
                y -= 1
        elif direc == 2: # 위쪽으로 이동
            if x <= 0:
                x = n - 1
            else:
                x -= 1
        elif direc == 3: # 아래쪽으로 이동
            if x >= n - 1:
                x = 0
            else:
                #print("heelo")
                x += 1

        #print(x, y)
        return x, y

    def check(visited):
        for i in range(n):
            if 1000 in visited[i]: # 100번 이상 반복한 경우 탈출 못하는거니까 안된다. 
                return False
        return True 


    ans = []
    q = deque()
    q.append((x, y, direc))

    while q:
        x, y, direc = q.popleft()
        print(x, y, direc)
        if graph[x][y] == '@':
            ans.append('YES')
            break

        if not check(visited):
            continue

        value = graph[x][y]
        #print(x, y, value, direc)
    
        if value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            memory = value
        elif value == '>':
            direc = 0
        elif value == '<':
            direc = 1
        elif value == '^':
            direc = 2
        elif value == 'v':
            direc = 3
        elif value == '_':
            if memory == '0' :
                direc = 0
            else:
                direc = 1
        elif value == '|':
            if memory == '0':
                direc = 3
            else:
                direc = 2
        elif value == '?':
            for i in range(4):
                nx, ny = get_next(x, y, i)
                q.append((nx, ny, i))
                visited[nx][ny] += 1
            continue

        elif value == '+':
            if memory == '15':
                memory = '0'
            else:
                memory = str(int(memory) + 1)
        elif value == '-':
            if memory == '0':
                memory = '15'
            else:
                memory = str(int(memory) - 1)

        nx, ny = get_next(x, y, direc)
        q.append((nx, ny, direc))
        visited[nx][ny] += 1
    
    if 'YES' in ans:
        return 'YES'
    else:
        return 'NO'
    #print(ans)
        


def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#"+str(i + 1), result)
        
if __name__ ==  "__main__":
    main()