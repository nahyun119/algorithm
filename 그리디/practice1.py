# 공포도 순서대로 정렬을 한 후,
# 공포도가 낮은 애들끼리 묶고, 다른 애들을 그룹화
# 이 때 현재 공포도 리스트에서 최대값이 공포도 리스트 길이보다 큰 경우는 그룹화를 할 수 없으므로
# break 한다. 

import time 

def main():
    N = int(input())
    degree_list = list(map(int, input().split()))

    degree_list.sort()

    count = 0
    result = 0

    start_time = time.time()

    while len(degree_list) != 0:
        max_deg = max(degree_list)
        if max_deg > len(degree_list):
            break
        for i in range(max_deg):
            degree_list.pop()
        count += 1

    # 정답 
    # 그냥 순서대로 정렬한 후, 하나씩 그룹에 넣고 확인하면 된다. 
    # 순서대로 정렬을 한 것이므로 최소한의 모험가를 이루게 되어 최대한의 그룹 수를 도출할 수 있다. 
    
    # for value in degree_list:
    #     count += 1 # 그룹에 포함되는 사람 수 
    #     if count >= value: # 공포도 그룹 조건을 만족하므로 그룹 결성 완료 
    #         result += 1
    #         count = 0
    
    end_time = time.time()
    print(count)
    print(end_time - start_time)

if __name__ ==  "__main__":
    main()   
