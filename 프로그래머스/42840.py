def solution(answers):
    answer = []
    
    person_01 = [1, 2, 3, 4, 5]
    person_02 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_03 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    n_1 = len(person_01)
    n_2 = len(person_02)
    n_3 = len(person_03)
    
    count = [0] * 3
    
    for i in range(len(answers)):
        if person_01[i % n_1] == answers[i]:
            count[0] += 1
        if person_02[i % n_2] == answers[i]:
            count[1] += 1
        if person_03[i % n_3] == answers[i]:
            count[2] += 1
            
    #print(count)
    
    max_value = max(count)
    
    for i in range(len(count)):
        if count[i] == max_value:
            answer.append(i + 1)
    
    return answer