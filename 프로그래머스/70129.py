def solution(s):
    answer = []

    count = 0
    remain = 0
    #print(int("0b110010101001", 2))
    while True:
        if int('0b' + s, 2) == 1:
            break 
        temp = len([x for x in s if x == '1'])
        remain += len(s) - temp
        s = str(bin(temp))
        s = s[2:]
        count += 1
        
        
    answer = [count, remain]
        
    return answer