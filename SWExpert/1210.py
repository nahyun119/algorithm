# 끝에서부터 차례대로 올라간다. 

from collections import deque
def solve():
    T = int(input())
    start = []
    graph = []
    for i in range(10):
        graph.append(list(map(int, input().split())))
    
    
    x = 99
    y = graph[99].index(2)

    dx = [0, 0, -1]
    dy = [-1, 1, 0] 


    while True:
        if x == 0:
            print("#" + str(T), y)
            break 
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < 100 and ny >= 0 and ny < 100:
                if graph[nx][ny] == 1:
                    x = nx
                    y = ny
                    graph[nx][ny] = 0
     

def main():
    for _ in range(1):
        solve()



if __name__ ==  "__main__":
    main()