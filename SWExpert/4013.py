T = int(input())
def clockwise(m):
    last = m[-1]
    m = [last] + m[:len(m) - 1]
    return m 

def counterclockwise(m):
    first = m[0]
    m = m[1:] + [first]
    return m

def check(number, direc, visited):
    global m
    visited[number - 1] = direc 
    #print(visited)

    if number == 1:
        if m[0][2] != m[1][6] and visited[1] == 0:
            check(2, -direc, visited)
    if number == 2:
        if m[0][2] != m[1][6] and visited[0] == 0:
            check(1, -direc, visited)
        if m[2][6] != m[1][2] and visited[2] == 0:
            check(3, -direc, visited)
    if number == 3:
        if m[1][2] != m[2][6] and visited[1] == 0:
            check(2, -direc, visited)
        if m[3][6] != m[2][2] and visited[3] == 0:
            check(4, -direc, visited)
    if number == 4:
        if m[2][2] != m[3][6] and visited[2] == 0:
            check(3, -direc, visited)
    return visited
        

for t in range(T):
    k = int(input())
    m = []
    for _ in range(4):
        m.append(list(map(int, input().split())))

    # m1 = list(map(int, input().split()))
    # m2 = list(map(int, input().split()))
    # m3 = list(map(int, input().split()))
    # m4 = list(map(int, input().split()))

    

    for i in range(k):
        number, direc = map(int, input().split())
        visited = check(number, direc, [0] * 4)
        for i in range(4):
            if visited[i] != 0:
                if visited[i] == 1:
                    m[i] = clockwise(m[i])
                else:
                    m[i] = counterclockwise(m[i])
        # print(visited)
        # print(m)
    
    result = 0
    for i in range(4):
        if m[i][0] == 1:
            result += (2 ** i)
    
    print("#" + str(t + 1), result)


        