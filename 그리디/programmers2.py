import numpy

def solution(number, k):
    answer = ''
    
    number_list = list(number)
    ori_num = len(number)
    
    
    for i in range(k):
        for index in range(len(number) - 1): 
            if(number_list[index] == '9'):
                continue
            if(number_list[index] == '1'):
                number_list.pop(index)
                break
            if(number_list[index] < number_list[index + 1]):
                number_list.pop(index)
                break
                
    # 다 삭제되지 않은 경우 -> 같은 숫자가 존재한다는 의미 
    updated_len = len(number_list)
    for i in range(k - (ori_num - updated_len)):
        for value in range(1, 10):
            if str(value) in number_list:
                number_list.remove(str(value))
                break
                
        
    
    answer = "".join(number_list)
    return answer