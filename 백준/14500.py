# dfs 이용해서 진행하려고 했는데,
# ㅓ 모양이 안되는 것 같다. 단순 무식하게 모든 경우의 수를 다 고려할 필요가 있는건가..

import sys
import heapq
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    graph = []
    max_list = []
    max_value = 0
    for i in range(n):
        temp = list(map(int, input().split()))
        # 최댓값 분리 
        if max_value < max(temp):
            max_value = max(temp)
            max_list = []
            for index, value in enumerate(temp):
                if value == max_value:
                    max_list.append((i, index))
        else:
            for index, value in enumerate(temp):
                if value == max_value:
                    max_list.append((i, index))
        
        graph.append(temp)
    

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = []

    for value in max_list:
        x, y = value[0], value[1]
        total = graph[x][y]
        visited = [(x, y)]
        pre = []
        for i in range(3): # 테트로미노는 정사각형 4개이므로 
            q = []
            for j in range(4): # 이동할 수 있는 상하좌우 
                nx = x + dx[j]
                ny = y + dy[j]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in visited:
                    heapq.heappush(q, (-graph[nx][ny], (nx, ny)))
            node = heapq.heappop(q)
            if pre:
                pre_node = heapq.heappop(pre)
                if -pre_node[0] > -node[0]:
                    total += -pre_node[0]
                    x = pre_node[1][0] 
                    y = pre_node[1][1]
                else:
                    total += -node[0]
                    x = node[1][0] 
                    y = node[1][1]
                    pre = q[:]
            else:
                total += -node[0]
                x = node[1][0] 
                y = node[1][1]
                pre = q[:]
            visited.append((x, y))
            
        result.append(total)

    print(max(result))
                




if __name__ ==  "__main__":
    main()