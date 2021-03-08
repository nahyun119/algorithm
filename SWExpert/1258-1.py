# 시간을 줄여보자
# 이전에는 dfs 를 이용해서 풀었는데 이번엔 0이 아닌 곳을 중심으로 행 크기와 열 크기를 각각 구한 후,
# 구한 후에 방문한 곳을 0으로 만들었다. 

import heapq
def solve():
    n = int(input())

    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    def change(x, y, ex, ey):
        for i in range(ex):
            for j in range(ey):
                matrix[x + i][y + j] = 0
    


    def find_matrix(x, y):
        row = 0
        col = 0
        for i in range(y, n):
            if matrix[x][i] > 0:
                #print(x, i)
                row += 1
                #matrix[x][i] = 0
            else:
                break 
        for i in range(x, n):
            if matrix[i][y] > 0:
                #print(i, y)
                col += 1
                #matrix[i][y] = 0 # 다시 방문하면 안되니까 
            else:
                break 

        change(x, y, col, row) # 방문한 곳을 모두 0으로 바꾼다. 
        return col, row

    result = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                x, y = find_matrix(i, j)
                #print(x, y, i, j)
                heapq.heappush(result, (x * y, x, y))
    
    answer = [len(result)]
    while result:
        size, x, y = heapq.heappop(result)
        answer.append(x)
        answer.append(y)
    
    return answer 

def main():
    T = int(input())
    for i in range(T):
        result = solve()
        print("#" + str(i + 1), *result)

if __name__ ==  "__main__":
    main()