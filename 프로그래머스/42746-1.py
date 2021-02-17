# 숫자들을 같은 자리수로 늘린다음
# 비교해서 오름차순 정렬을 한다.
# 이 때 numbers가 모두 0이라면 
# 0을 리턴하도록 한다. 

def solution(numbers):
    answer = ''
    
    # numbers 원소는 최대 3자리이므로 모든 숫자를 6자리로 만든다
    
    str_numbers = list(map(str, numbers))
    new_numbers = []
    
    for number in str_numbers:
        length = len(number)
        new_numbers.append((number * (6 // length), number))
    
    new_numbers.sort(reverse = True)
    result = ''
    
    if new_numbers[0][1] == '0': # 정렬했는데도 앞이 0이라면 0을 리턴 
        return '0'
    
    for value in new_numbers:
        result += value[1]
    
    answer = result     
    return answer