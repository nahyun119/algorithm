# arrow를 이용해서 노드랑 간선을 구하는 것까지는 구현을 했는데,,
# 방을 만드는지 유무를 판단하는 코드를 작성하기가 애매하다..
# 그래프처럼 간선이 추가될 때마다 cycle이 발생하는지 확인하는식으로 했는데 이 방법이 아닌가보다 ㅠ 

def solution(arrows):
    answer = 0
    
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    
    hash_map = {}
    
    hash_map[(0, 0)] = [] # 1번 노드 
    
    x = 0
    y = 0
    
    nodes = [(0, 0)]
    
    for arrow in arrows:
        nx = x + dx[arrow]
        ny = y + dy[arrow]
        if (nx, ny) in hash_map:
            hash_map[(nx, ny)].append((x, y))
        else:
            nodes.append((nx, ny)) # 순서대로 
            hash_map[(nx, ny)] = [(x, y)]
        x = nx 
        y = ny
    
    edges = []
    
    for index, node in enumerate(nodes):
        for value in hash_map[node]:
            i = nodes.index(value)
            edges.append((index + 1, i + 1))
            
    result = 0
    v = len(nodes)
    parent = [0] * (v + 1)

    answer = result
        
    return answer