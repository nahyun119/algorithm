import itertools
def is_prime(number):
    for i in range(1, number + 1):
        if number % i == 0 and (i != number and i != 1): # 자기 자신과 1이 아닌 경우에 나눠지면 소수 아님 
            return False 
    return True
            

def solution(numbers): 
    answer = 0
    
    number_list = list(numbers)
    
    result = []
    for number in number_list:
        if is_prime(int(number)) and int(number) != 1 and int(number) != 0 and int(number) not in result: # 한 자리수인 경우 
            result.append(int(number))
            
            
    for i in range(2, len(numbers) + 1): # 2자리 숫자부터
        per_list = list(map(''.join, itertools.permutations(number_list, i)))
        per_set = set(per_list)
        per_list = list(per_set) # 중복 제거 
        #print(per_list)
        for p in per_list:
            if is_prime(int(p)) and int(p) != 1 and int(p) != 0 and int(p) not in result:
                result.append(int(p))
    #print(result)
    #print(count)
    answer = len(result)
    return answer