# 우선순위 큐를 이용해서 진행하면 그리디 방법으로 해결할 수 있다.
# 나중에 더 분석해보자 
import heapq

def main():
    food_times = list(map(int, input().split()))
    K = int(input())

    sum_foods = sum(food_times)

    if sum_foods <= K:
        return -1

    food_heap = []
    for index in range(len(food_times)):
        heapq.heappush(food_heap, (food_times[index], index + 1))

    sum_values = 0
    previous = 0

    length = len(food_times)

    # while sum_values + ((food_heap[0][0] - previous) * length) <= K:
    #     print(food_heap)
    #     pop_food = heapq.heappop(food_heap)
    #     print(pop_food, sum_values)
    #     now = pop_food[0]
    #     sum_values += (now - previous) * length
    #     length -= 1
    #     previous = now
    # print(food_heap, K - sum_values)
    # result = sorted(food_heap, key = lambda x:x[1])
    # print(result[(K - sum_values) % length][1])
    # # print(food_heap)
    
    turn_time = 0
    while sum_values <= K:
        remain_food = len(food_heap)
        remove_food = heapq.heappop(food_heap)
        print(remove_food)
        temp = sum_values + remain_food * remove_food[0]
        temp = temp - (remain_food * turn_time)
        print(temp)
        if temp <=  K :
            food_times.pop(remove_food[1] - 1)
            sum_foods = sum(food_times)
            turn_time += 1
            sum_values = temp
        else :
            heapq.heappush(food_heap, remove_food)
            
            break
        
    remain_foods = len(food_times)

    food_heap.sort(key=lambda x:x[1])
    last_foods = food_heap[K % remain_foods]
    print(K - sum_values)
    print(food_heap[(K - sum_values) % remain_foods][1])

    # # if K > remain_foods:
    # #     last_foods = food_heap[(K + 1) % remain_foods + 1]
    # # else:
    # #     last_foods = food_heap[K]
    # # last_foods = food_heap[(remain_foods + 1) % K ]



    
    
if __name__ ==  "__main__":
    main() 