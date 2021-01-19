from itertools import combinations

def main():
    N, M = map(int, input().split())

    graph = []
    for value in range(N):
        graph.append(list(map(int, input().split())))
    
    home = []
    chicken = []

    for i in range(N): # 치킨집, 일반집 데이터 담기 
        for j in range(N):
            if graph[i][j] == 2:
                chicken.append((i, j))
            if graph[i][j] == 1:
                home.append((i, j))

    item = []
    for value in range(len(chicken)):
        item.append(value)
    
    combination_ch = list(combinations(item, M)) # 치킨 집 조합 구하기 

    distance = [[0] * len(chicken) for _ in range(len(home))]
                    
    for index, h in enumerate(home): # 치킨 집과 일반 집과의 모든 거리 구하기 
        for c_index, c in enumerate(chicken):
            dis = abs(h[0] - c[0]) + abs(h[1] - c[1])
            distance[index][c_index] = dis

    d_result = [] # 가능한 모든 조합들 중에서 도시 치킨 거리 구하기 
    for value in combination_ch:
        result = 0
        for i in range(len(home)):
            d_min = 9999
            for index in range(M):
                dis = distance[i][value[index]] 
                if d_min > dis:
                    d_min = dis
            result += d_min 
        d_result.append(result)
    #print(d_result)

    print(min(d_result))

if __name__ ==  "__main__":
    main()    