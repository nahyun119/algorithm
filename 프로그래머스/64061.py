def solution(board, moves):
    answer = 0
    stack = []
    length = len(board)
    for move in moves:
        for i in range(length):
            if board[i][move - 1] != 0:
                #print(move, board[i][move - 1])
                if not stack: # 스택이 빈 경우 
                    stack.append(board[i][move - 1])
                else: # 스택이 있는 경우 
                    if stack[-1] == board[i][move - 1]: # 같은 경우 
                        answer += 2 
                        stack.pop()
                    else:
                        stack.append(board[i][move - 1])
                board[i][move - 1] = 0        
                break
        #print(move, stack)
        
    return answer