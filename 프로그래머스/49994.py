def change_dirs(d):
    if d == 'U':
        return 0
    elif d == 'D':
        return 1
    elif d == 'R':
        return 2
    else:
        return 3
    
def solution(dirs):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visited = []
    x = 0
    y = 0
    
    for d in dirs:
        dire = change_dirs(d)
        nx = x + dx[dire]
        ny = y + dy[dire]
        if nx >= -5 and nx <= 5 and ny >= -5 and ny <= 5:
            v = set([(x, y), (nx, ny)])
            if v not in visited:
                visited.append(v)
            #print(x, y, nx, ny)
            x = nx 
            y = ny
    
    #print(len(visited))  
    answer = len(visited)
    return answer