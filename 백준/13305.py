def main():
    n = int(input())
    distance = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    total = 0
    c_distance = distance[0]
    c_cost = cost[0] 
    for i in range(1, n - 1):
        if c_cost > cost[i]:
            total += c_cost * c_distance
            c_distance = distance[i]
            c_cost = cost[i]
        else:
            #c_cost = cost[i]
            c_distance += distance[i]

    if total == 0: #맨처음이 제일 작은 경우
        total = c_cost * c_distance
    else:
        total += c_cost * c_distance # 마지막 더하기 

    print(total)




if __name__ ==  "__main__":
    main()