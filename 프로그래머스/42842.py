import itertools 
# permutations은 자기 자신이랑 다른 원소랑 조합
# product는 자기 자신이랑도 조합 가능 

# 맨처음에는 x, y 조합에 대해서 모두 고려했는데, 시간이 너무 오래 걸렸다
# 근데 생각해보니 x나 y에 대해서 하나만 알면 yellow, brown을 이용해서 다른 하나를 구할 수 있기때문에
# 하나에 대해서만 반복문을 돌려서 모든 경우를 탐색하면 된다. 

def solution(brown, yellow):
    answer = []
    max_value = max(brown, yellow)
    
    number_list = []
    
    for i in range(1, max_value + 1):
        number_list.append(i)
    
    
    result = []
    
    for x in number_list:
        y_1 = (brown + 4 - 2 * x) / 2
        if (x - 2) > 0:
            y_2 = (yellow / (x - 2) + 2)
        else:
            y_2 = 0
        if y_1 == y_2 and x >= y_1:
            #print(x, y_1, y_2)
            result.append(x)
            result.append(int(y_1))
               
    #print(result)
    answer = result
    return answer