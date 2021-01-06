# 너무 간단한데, 효율성 문제가 있지않을까 생각한다. 
# n^2 만큼 걸릴거같아서 그러면 1000000 만큼의 연산 

import copy
import time 

def main():
    start_time = time.time()

    N, M = map(int, input().split())
    ball_list = list(map(int, input().split()))

    count = 0 

    for first_index in range(len(ball_list)):
        for second_index in range(first_index, len(ball_list)):
            if ball_list[first_index] != ball_list[second_index]:
                count += 1
    
    print(count)
    end_time = time.time()

    print(end_time - start_time)

if __name__ ==  "__main__":
    main()  
