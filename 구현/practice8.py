from itertools import permutations
def solution(n, weak, dist):
    answer = 0
    
    wall = [0] * (len(weak) * 2)
    
    for i in range(len(weak)):
        wall[i] = weak[i]
        wall[i + len(weak)] = weak[i] + n
#     print(wall)

#     print(len(weak))
    
    combination_f = list(permutations(dist, len(dist)))
    answer = len(dist) + 1
    
    for index in range(len(weak)):
        for friend in combination_f:
            count = 1
            end = wall[index] + friend[count - 1] # 친구가 갈 수 있는 마지막 위치
            for value in range(index, index + len(weak)):
                if end < wall[value]: # 점검할 수 있는 위치를 벗어난 경우
                    count += 1
                    if count > len(dist): # 모두 투입한 경우 종료 
                        break
                    end = wall[value] + friend[count - 1]
            answer = min(answer, count)
            
    if answer > len(dist):
        return -1
    return answer