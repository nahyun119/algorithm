import sys
input = sys.stdin.readline

def main():

    n, m, x, y, k = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dice = [0] * 7 # 위, 아래, 앞, 뒤, 왼, 오

    orders = list(map(int, input().split()))


    for order in orders:

        if order == 1: # 동쪽 이동 
            nx = x
            ny = y + 1
            if nx >= 0 and nx < n and ny >= 0 and ny < m: # 범위 안에 
                dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
                if graph[nx][ny] != 0:
                    dice[1] = graph[nx][ny] # 현재 주사위의 아래 부분은 그래프의 값 흡수 
                    graph[nx][ny] = 0
                else:
                    graph[nx][ny] = dice[1] # 0인 경우 주사위 바닥면이 그래프로 흡수 

                x = nx
                y = ny
                    
                print(dice[6]) # 현재 위 

        elif order == 2: # 서쪽 이동 
            nx = x
            ny = y - 1
            if nx >= 0 and nx < n and ny >= 0 and ny < m: # 범위 안에 
                dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
                if graph[nx][ny] != 0:
                    dice[1] = graph[nx][ny] # 현재 주사위의 아래 부분은 그래프의 값 흡수 
                    graph[nx][ny] = 0
                else:
                    graph[nx][ny] = dice[1] # 0인 경우 주사위 바닥면이 그래프로 흡수 

                x = nx
                y = ny
                    
                print(dice[6]) # 현재 위 

        elif order == 3: # 북쪽 이동 
            nx = x - 1
            ny = y
            if nx >= 0 and nx < n and ny >= 0 and ny < m: # 범위 안에 
                dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
                if graph[nx][ny] != 0:
                    dice[1] = graph[nx][ny] # 현재 주사위의 아래 부분은 그래프의 값 흡수 
                    graph[nx][ny] = 0
                else:
                    graph[nx][ny] = dice[1] # 0인 경우 주사위 바닥면이 그래프로 흡수 

                x = nx
                y = ny
                    
                print(dice[6]) # 현재 위 

        elif order == 4: # 남쪽 이동 
            nx = x + 1
            ny = y
            if nx >= 0 and nx < n and ny >= 0 and ny < m: # 범위 안에 
                dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
                if graph[nx][ny] != 0:
                    dice[1] = graph[nx][ny] # 현재 주사위의 아래 부분은 그래프의 값 흡수 
                    graph[nx][ny] = 0
                else:
                    graph[nx][ny] = dice[1] # 0인 경우 주사위 바닥면이 그래프로 흡수 

                x = nx
                y = ny
                    
                print(dice[6]) # 현재 위 

    


    # for order in orders:
    #     if order == 1: # 동쪽 이동 
    #         nx = x
    #         ny = y + 1
    #         if nx >= 0 and nx < n and ny >= 0 and ny < m: # 범위 안에 
    #             up = current[4] # 윗면이 원래 왼쪽 부분 
    #             front = current[2] # 앞면은 그대로
    #             for value in hash_map[up]:
    #                 if value[2] == front:
    #                     current = value # 현재 모양 업데이트 
    #             if graph[nx][ny] != 0:
    #                 dice[current[1] - 1] = graph[nx][ny] # 현재 주사위의 아래 부분은 그래프의 값 흡수 
    #             graph[nx][ny] = 0
    #             x = nx
    #             y = ny
                
    #             print(dice[current[0] - 1]) # 현재 위 

    #     elif order == 2: # 서쪽 이동 
    #         nx = x
    #         ny = y - 1
    #         if nx >= 0 and nx < n and ny >= 0 and ny < m: # 범위 안에 
    #             up = current[5] # 윗면이 원래 오른쪽 부분 
    #             front = current[2] # 앞면은 그대로
    #             for value in hash_map[up]:
    #                 if value[2] == front:
    #                     current = value # 현재 모양 업데이트 
    #             if graph[nx][ny] != 0:
    #                 dice[current[1] - 1] = graph[nx][ny] # 현재 주사위의 아래 부분은 그래프의 값 흡수 
    #             graph[nx][ny] = 0
    #             x = nx
    #             y = ny
                
    #             print(dice[current[0] - 1]) # 현재 위 

    #     elif order == 3: # 북쪽 이동 
    #         nx = x - 1
    #         ny = y
    #         if nx >= 0 and nx < n and ny >= 0 and ny < m: # 범위 안에 
    #             up = current[2] # 윗면이 원래 앞부분 
    #             front = current[1] # 앞면이 원래 아래부분
    #             for value in hash_map[up]:
    #                 if value[2] == front:
    #                     current = value # 현재 모양 업데이트 
    #             if graph[nx][ny] != 0:
    #                 dice[current[1] - 1] = graph[nx][ny] # 현재 주사위의 아래 부분은 그래프의 값 흡수 
    #             graph[nx][ny] = 0
    #             x = nx
    #             y = ny
                
    #             print(dice[current[0] - 1]) # 현재 위 
    #     elif order == 4: # 남쪽 이동 
    #         nx = x + 1
    #         ny = y
    #         if nx >= 0 and nx < n and ny >= 0 and ny < m: # 범위 안에 
    #             up = current[3] # 윗면이 원래 뒷부분 
    #             front = current[0] # 앞면이 원래 윗면
    #             for value in hash_map[up]:
    #                 if value[2] == front:
    #                     current = value # 현재 모양 업데이트 
    #             if graph[nx][ny] != 0:
    #                 dice[current[1] - 1] = graph[nx][ny] # 현재 주사위의 아래 부분은 그래프의 값 흡수 
    #             graph[nx][ny] = 0
    #             x = nx
    #             y = ny
    #             print(dice[current[0] - 1]) # 현재 위 
    #     #print(dice, current, order)

                



if __name__ ==  "__main__":
    main()