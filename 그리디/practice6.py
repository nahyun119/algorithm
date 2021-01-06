# 테스트케이스는 모두 통과하지만
# 효율성 테스트에서 탈락 

def main():
    food_times = list(map(int, input().split()))
    K = int(input())

    num_foods = len(food_times)

    last_food = 0
    
    # 전체 먹는 시간보다 \
    if K > sum(food_times):
        return -1
    
    for value in range(K):
        if(food_times[last_food] != 0):
            food_times[last_food] -= 1
            last_food = (last_food + 1) % num_foods
        else:
            last_food = (last_food + 1) % num_foods
            # 더 섭취해야하는 음식까지 탐색 
            # 음식을 모두 살펴봤는데 모두 0인 경우 -1 출력하고 종료 
            turn_time = 1
            while food_times[last_food] == 0:
                if(turn_time >= num_foods):
                    return -1
                last_food = (last_food + 1) % num_foods
                turn_time += 1
            food_times[last_food] -= 1
            
            # 줄인 다음에 다음 인덱스로 갱신해야 
            last_food = (last_food + 1) % num_foods
            

    # 네트워크 복구 후 다시 먹을 음식 탐색 
    # 다시 먹을 음식이 없는 경우 -1 출력하고 종료하도록 
    
    turn_time = 1
    while food_times[last_food] == 0:
        if(turn_time >= num_foods):
            return -1
        last_food = (last_food + 1) % num_foods
        turn_time += 1

    answer = last_food + 1
    return answer

if __name__ ==  "__main__":
    main() 