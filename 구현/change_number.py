# 원하는 진법 변환하는 코드 
# 파이썬에서 지원하는 bin, oct, hex이 있지만 이 아이들은 10진법을 해당 진법으로 변경
# int(변환할 문자열, 8) 이렇게하면 변환할 문자열을 8진수라 생각해서 그에 맞게 10진수로 변경 

n = int(input())
def conv(number, n): # 숫자와 변환할 진법
    # T = '0123456789' # n이 10이하라면 이렇게 
    T = '0123456789ABCDEF' # n이 16이하라면 

    q, r = divmod(number, n)
    if q == 0: # 몫이 0이면 나머지에 대한 숫자만 반환 
        return T[r]
    else:
        return conv(q, n) + T[r] # 몫이 0이 아니면 재귀 이용 


print(conv(n, 16))