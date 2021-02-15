from itertools import chain

def solution(board):

    
    answer = 0      
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            min_value = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1])
            #print(i, j, min_value)
            if min_value == 0 or board[i][j] == 0:
                continue
            
            board[i][j] = max(min_value + 1, board[i][j])
            
            # if board[i][j] > answer:
            #     answer = board[i][j]
            
    answer = max(list(chain.from_iterable(board))) ** 2 # 여러 차원의 배열을 일차원으로 만드는 chain.from_iterable
    #answer = answer * answer
    
    
    return answer