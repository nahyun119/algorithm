# 맨 처음에 while문 조건을 0 in check 로 했는데
# 효율성 테스트에서 시간 초과가 떴다.
# 그래서 while 문을 first_index < last_index로 변경 후
# 마지막에 check가 안된 부분이 있다면 걔는 혼자서 보트를 보내야하는 애이기 때문에 count += 1을 했다.
# 그랬더니 효율성 통과~~ 

def solution(people, limit):
    answer = 0
    
    people.sort()
    
    check = [0] * len(people)
    
    last_index = len(people) - 1
    first_index = 0
    
    count = 0
    
    if len(people) == 1:
        return 1
    
    while first_index < last_index:
        # if first_index >= last_index:
        #     count += 1 
        #     check[first_index] = 1
        #     break
        if people[first_index] + people[last_index] <= limit:
            count += 1 
            check[first_index] = 1
            check[last_index] = 1
            first_index += 1 
            last_index -= 1
        else:
            check[last_index] = 1
            count += 1
            last_index -= 1
            
    if 0 in check:
        count += 1 
    #print(first_index, last_index, count)
    answer = count 
    return answer