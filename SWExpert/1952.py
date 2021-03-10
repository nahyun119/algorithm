# 재귀를 이용해서 모든 경우를 탐색 

T = int(input())

def calculate(month, value):
    global min_value
    #print(month, value)
    if month >= 12:
        if min_value > value:
            min_value = value 
        return 
    
    calculate(month + 1, value + plan[month] * cost[0]) # 1일 이용권 
    calculate(month + 1, value + cost[1]) # 1달 이용권 
    calculate(month + 3, value + cost[2]) # 3달 이용권 -> 이번달에 계산하면 month + 1, month +2 는 계산할필요 없으므로 


for t in range(T):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    min_value = 1e9
    # 완전 탐색? 
    calculate(0, 0)
    min_value = min(min_value, cost[3])
    print("#" + str(t + 1), min_value)