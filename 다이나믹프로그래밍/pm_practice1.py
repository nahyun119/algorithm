# 프로그래머스 다이나믹 프로그래밍 1번

def solution(N, number):
    answer = 0

    avail = []
    
    for i in range(1, 9): # 8번 시행 
        #print(avail)
        num = 0
        for k in range(i):
            num = num * 10 + N
            
        avail_number = set([num])
        
        for j in range(0, i -1):
            for x in avail[j]:
                for y in avail[-j - 1]:
                    avail_number.add(x + y)
                    avail_number.add(x * y)
                    avail_number.add(x - y)
                    
                    if x != 0:
                        avail_number.add(y // x)
                    if y != 0:
                        avail_number.add(x // y)
                        
        #print(avail_number)
        if number in avail_number:
            return i
        
        avail.append(avail_number)
    
    return -1