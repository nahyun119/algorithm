# 테스트 케이스는 통과하는데 시간초과~~


def solution(numbers):
    answer = ''
    
    result = [str(numbers[0])]
    max_value = numbers[0]
 
    for i in range(1,len(numbers)):
        temp = result[:]
        for j in range(len(temp) + 1):
            temp.insert(j, str(numbers[i]))
            int_value = int(''.join(temp))
            #print(max_value, int_value, result)
            if max_value < int_value:
                result = temp[:]
                max_value = int_value
            temp.pop(j)
            
    #print(result)          
    answer = ''.join(result)       
            
    return answer