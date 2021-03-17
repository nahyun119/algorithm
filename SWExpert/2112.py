T = int(input())
def check(board, k): # 성능 검사 
    for i in range(w):
        stack = []
        flag = False
        for j in range(d + 1):
            if len(stack) >= k:
                flag = True 
                break 
            if j >= d:
                break
            if not stack:
                stack.append(board[j][i])
            else:
                #print(j, i)
                if stack[-1] == board[j][i]: # 같으면 넣는다.
                    stack.append(board[j][i])
                else: # 다르면 스택을 비우고 값을 넣는다. 
                    stack = []
                    stack.append(board[j][i])
        if flag:
            continue 
        else:
            return i # 성능 검사 실패한 열 
    return -1 # 모두 성능 검사를 통과하면 -1 

def dfs(b, count, row, k): # 모든 행에 대해서 다 탐색을 진행한다. 
    global min_value 
    
    if count < min_value:
        if check(b, k) == -1:
            min_value = count 
            return 
    else:
        return 
    
    for i in range(row + 1, d):
        if count + 1 < min_value: # 한번 더 했는데도 최솟값보다 작으면, 만약 같거나 크면 굳이 탐색할 필요없으므로 
            temp = b[i][:]
            b[i] = [0 for _ in range(w)] # a type
            dfs(b, count + 1, i, k)

            board[i] = [1 for _ in range(w)] # b type 
            dfs(b, count + 1, i, k)

            board[i] = temp # 복원 
    


for t in range(T):
    d, w, k = map(int, input().split())
    board = []
    for i in range(d):
        board.append(list(map(int, input().split())))

    min_value = 1e9


    if k == 1: # 1인 경우 약물을 투여할 필요 없다.
        print("#" + str(t + 1), 0) 
        continue
    
    if check(board, k) == -1:
        print("#" + str(t + 1), 0)
        continue

    for i in range(d):
        temp = board[i][:]
        board[i] = [0 for _ in range(w)] # a type
        dfs(board, 1, i, k)

        board[i] = [1 for _ in range(w)] # b type
        dfs(board, 1, i, k)
        board[i] = temp 

    print("#" + str(t + 1), min_value)
    





