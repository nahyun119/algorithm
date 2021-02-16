# 맨 처음에는 숫자 순서도 고려해서 생각을 했는데
# 숫자의 순서에 상관없이 동일한 수식이기 때문에 순서를 굳이 고려할 필요가 없다.
# 그냥 순서대로 numbers 탐색하면 된다. 
# 너무 어렵게 생각해했다..


count = 0 

def solution(numbers, target):
    global count 
    answer = 0 
    length = len(numbers)
    
    def dfs(number, index):
        global count 
        
        if index == length - 1: # 다 탐색한 경우 종료
            if number == target:
                count += 1
            return 
        else:
            dfs(number - numbers[index + 1], index + 1)
            dfs(number + numbers[index + 1], index + 1)
    
    
    # 숫자의 순서는 상관이 없을듯 
    dfs(numbers[0], 0)
    dfs(-1 * numbers[0], 0)
    
    answer = count
    
    
    return answer