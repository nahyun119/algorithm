import sys


def main():

    sys.setrecursionlimit(10**7) 

    N, M = map(int, input().split())

    ice_list = []
   
    for value in range(N):
        ice_list.append(list(map(int, input())))

    def dfs(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return False 
        if ice_list[x][y] == 0:
            ice_list[x][y] = 1
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        return False 

    result = 0 
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result += 1

    print(result)
if __name__ ==  "__main__":
    main()

