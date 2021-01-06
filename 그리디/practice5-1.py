# practice 5번 다시 구현 

import copy
import time 

def main():
    start_time = time.time()

    N, M = map(int, input().split())
    ball_list = list(map(int, input().split()))

    result = 0 

    num_list = [0] * 11 # M이 1에서 10까지이므로 
    for value in ball_list:
        num_list[value] += 1
    
    
    for value in range(1, M + 1):
        #print(value, result)
        result += num_list[value] * (N - num_list[value])
        N -= num_list[value]
        num_list[value] = 0

    end_time = time.time()
    print(result)
    print(end_time - start_time)

if __name__ ==  "__main__":
    main()  
