import sys
import heapq 
input = sys.stdin.readline

# 맨처음에 quick sort를 이용해서 구현을 했는데
# 계속 메모리 초과 에러가 발생
# 그래서 혹시나해서 heapq를 이용했는데,,
# heapq로 하니까 통과,, 

# def quick_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers
    
#     pivot = numbers[0] # 맨 처음 원소를 pivot으로 
#     #num_list = numbers[1:] # 나머지 원소들은 list

#     return quick_sort([x for x in numbers[1:] if x <= pivot]) + [pivot] + quick_sort([x for x in numbers[1:] if x > pivot])

def main():
    n = int(input())
    
    number_list = []
    for _ in range(n):
        #number_list.append(int(input()))
        heapq.heappush(number_list, int(input()))

    #numbers = quick_sort(number_list)

    while number_list:
        number = heapq.heappop(number_list)
        print(number)



if __name__ ==  "__main__":
    main()