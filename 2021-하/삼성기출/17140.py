import sys
import heapq

input = sys.stdin.readline 

r, c, k = map(int, input().split())

matrix = []
for i in range(3): # 초기 크기 3x3
    matrix.append(list(map(int, input().split())))

if 0 <= r - 1 < len(matrix) and 0 <= c - 1 < len(matrix[0]):
    if matrix[r - 1][c - 1] == k: # 연산하기 전에 k가 된다면
        print(0)
        exit()

count = 0 

def calculate(length, matrix):
    max_row = 0

    new_matrix = []

    for i in range(length):
        current_row = matrix[i]
        new_row = []
        hash_map = {}
        for j in current_row:
            if j == 0: #0은 무시
                continue
            if j in hash_map:
                hash_map[j] += 1
            else:
                hash_map[j] = 1
                
        counting = []
        for k in hash_map:
            counting.append((k, hash_map[k]))
            
        counting.sort(key = lambda x : (x[1], x[0]))
        for c in counting:
            new_row.append(c[0])
            new_row.append(c[1])
            
        new_matrix.append(new_row)

        if max_row < len(new_row):
            max_row = len(new_row)
        
    for i in range(length):
        if len(new_matrix[i]) < max_row:
            for j in range(max_row - len(new_matrix[i])):
                new_matrix[i].append(0)
    # print("####### 함수 내에서 확인 #####")
    # print(new_matrix)
    return new_matrix
        

while count < 100: # 100초까지 진행
    row = len(matrix)
    col = len(matrix[0])

    if row > 100:
        matrix = matrix[:100]
        row = 100
    if col > 100:
        matrix = [matrix[i][:100] for i in range(row)]
        col = 100

    new_matrix = []

    if row >= col: # R연산 
        new_matrix = calculate(row, matrix)
    else: # 열 연산
        trans_matrix = []

        for i in range(col): # 행 렬 전환 
            current_col = [matrix[j][i] for j in range(row)] #  i번째 열 
            trans_matrix.append(current_col)

        trans_matrix = calculate(col, trans_matrix)
        new_col = len(trans_matrix)
        new_row = len(trans_matrix[0])

        for i in range(len(trans_matrix[0])):
            current_col = [trans_matrix[j][i] for j in range(new_col)]
            new_matrix.append(current_col)

    matrix = new_matrix
    count += 1   
    # print(matrix, count)
    if 0 <= r - 1 < len(matrix) and 0 <= c - 1 < len(matrix[0]):
        if matrix[r - 1][c - 1] == k:
            print(count)
            exit()      

print(-1)
