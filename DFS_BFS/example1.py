def dfs(ice_list, x, y, visited):
    visited[x][y] = 1
    
    if x < 0 or x >= N or y < 0 or y >= M:
        return False 
    if visited[x][y] == 1:
        

def main():
    N, M = map(int, input().split())

    ice_list = []
   
    for value in range(N):
        ice_list.append(list(map(int, input())))
    
    visited = [[0] * M for _ in range(N)]
    
if __name__ ==  "__main__":
    main()

