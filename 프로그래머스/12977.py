import itertools

def is_prime(num):
    for i in range(2, num + 1):
        if num % i == 0 and num != i:
            return False
    return True

def solution(nums):
    answer = -1
    
    avail = []
    
    # 서로 다른 3개를 골라서 
    avail = list(itertools.combinations(nums, 3))
    count = 0
    for a in avail:
        if is_prime(sum(a)):
            count += 1
    #print(count)
        

    answer = count

    return answer