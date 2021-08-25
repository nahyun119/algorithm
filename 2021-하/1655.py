import sys 
import heapq
import math, copy

input = sys.stdin.readline 

N = int(input())


# 중간값을 기준으로 작은 값 (max_heap), 큰 값(min_heap) 해서 정렬하도록
# 따라서 중간 값을 기준으로 값을 삽입해서 max_heap 크기 >= min_heap 크기
# 중간 값 => max_heap 의 root 

min_heap = [] # 중간 값을 기준으로 큰 값
max_heap = [] # 중간 값을 기준으로 작은 값 


for i in range(N):
    number = int(input())
    
    if i == 0: # 첫번째 원소인 경우 
        heapq.heappush(max_heap, -number)    
        print(number)   

    else: # 나머지의 경우 
        if len(min_heap) == len(max_heap): # max_heap 크기가 min_heap 크기보다 커야하므로 원소를 max_heap에 넣는다
            heapq.heappush(max_heap, -number)
        else: # max_heap이 더 큰 경우 min_heap에 원소 넣기
            heapq.heappush(min_heap, number)
        
        min_n = heapq.heappop(min_heap) # 중간값보다 큰 값
        max_n = heapq.heappop(max_heap) # 중간값보다 작은 값 

        # 만약 max_n > min_n 인 경우 swap
        if -max_n > min_n:
            heapq.heappush(max_heap, -min_n)
            heapq.heappush(min_heap, -max_n)
        else:
            heapq.heappush(max_heap, max_n)
            heapq.heappush(min_heap, min_n)

        middle = heapq.heappop(max_heap) # 중간값은 max_heap의 top
        print(-middle)
        heapq.heappush(max_heap, middle)