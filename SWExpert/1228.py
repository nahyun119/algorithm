def solve():
    n = int(input())
    original = list(map(str, input().split()))
    # hash_map = {}
    # for i in range(len(original)):
    #     hash_map[i] = int(original[i])

    m = int(input()) # 명령어 수 
    order = input().strip()
    order = order.split(" ")
    
    order_list = []
    result = []
    for i in range(len(order)):
        if order[i] == 'I':
            if i != 0:
                order_list.append(result)
                result = []        
        else:
            result.append(order[i])
        #print(result)
    order_list.append(result)
    

    for i in range(m):
        x, y = int(order_list[i][0]), int(order_list[i][1])
        #print(x, y)
        if x == 0:
            temp = []
            for j in range(y):
                temp.append(order_list[i][2 + j])
            original = temp + original[:]
        else:
            temp = [original[x - 1]]
            for j in range(y):
                temp.append(order_list[i][2 + j])
        # print(temp)
        # print(original)
            original = original[: x - 1] + temp + original[x + 1:]
        # print(original)
        
    #print(original)  
    return original[: 10]
    


def main():
    for i in range(1):
        result = solve()
        print("#" + str(i + 1), *result)

if __name__ ==  "__main__":
    main()