from math import gcd, trunc, ceil # 최대공약수 

# 대각선을 잇는 일차방정식을 세우면 된다!!!!!
# 1억이라 너무 커서 최대공약수를 구해서 나눠서 진행했는데도 11번 테케에서 시간 초과 ㅠ


# 최대공약수랑 관련이 있다. 
# 잘라지는 사각형 수는 nw + nh - g(최대공약수) 임 ... -> 그래서 반복문을 돌릴 필요 없이 해결할 수 있는 것 
def solution(w,h):
    answer = 1
    
    n = gcd(w, h)
    
    nw = w // n
    nh = h // n
    
    pro = nh / nw
    
    count = 0
    
    # for i in range(1, nw + 1):
    #     pre = (i - 1) * pro
    #     now = i * pro
    #     count += (ceil(now) - trunc(pre))  
     
    answer = (w * h) - (nw + nh - n) * n
    return answer