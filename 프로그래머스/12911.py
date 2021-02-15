def solution(n):
    answer = 0
    
    bin_n = bin(n)
    bin_n = bin_n[2:]
    count_n = bin_n.count('1')
    
    temp = n
    #print(bin_n, count_1)
    while True:
        temp += 1
        bin_t = bin(temp)
        bin_t = bin_t[2:]
        if count_n == bin_t.count('1'):
            return temp 
        
    
    
    return answer