# 각 노드를 한번만 방문하고 회사 -> n개의 장소 -> 집으로 이동하는 최단 경로를 구하는 문제
# TSP 문제라고 한다.

INF = 1e9

def solve():
    n = int(input())
    position = list(map(int, input().split()))

    start = (position[0], position[1]) # 회사 
    end = (position[2], position[3]) # 집

    node = []


    for i in range(4, len(position), 2):
        node.append((position[i], position[i + 1]))
    
    graph = [[0] * (n + 2) for _ in range(n + 2)]

    # 0번째는 회사 
    # n + 1은 집 
    for i in range(n):
        graph[0][i + 1] = abs(start[0] - node[i][0]) + abs(start[1] - node[i][1])
        graph[i + 1][0] = abs(start[0] - node[i][0]) + abs(start[1] - node[i][1])
        graph[n + 1][i + 1] = abs(end[0] - node[i][0]) + abs(end[1] - node[i][1])
        graph[i + 1][n + 1] = abs(end[0] - node[i][0]) + abs(end[1] - node[i][1])
        for j in range(n):
            graph[i + 1][j + 1] = abs(node[i][0] - node[j][0]) + abs(node[i][1] - node[j][1])
    
    #print(graph)
    dp = [[INF] * (1 << n + 1) for _ in range(n + 1)]
    #print(dp)
    

    def find_path(last, visited): # 비트마스킹과 메모제이션을 이용한 TSP 
        # print(last, visited)
        #print(dp)
        if visited == (1 << n + 1) - 1: # 모두 방문한 경우
            return graph[last][n + 1]
        
        if dp[last][visited] != INF: # 이미 방문한 경우 
            return dp[last][visited]

        temp = INF
        for i in range(n + 1): # 모든 장소들에 대해서 
            if visited & (1 << i) == 0 and graph[last][i] != 0: # 아직 방문하지 않고 가는 경로가 있는 경우 
                temp = min(temp, find_path(i, visited | (1 << i)) + graph[last][i])
        dp[last][visited] = temp
        return temp

    value = find_path(0, 1 << 0)
    return value



def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()