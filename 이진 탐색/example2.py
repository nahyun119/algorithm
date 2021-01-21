def get_remain(foods, mid, target):
    sum_food = 0
    for i in range(mid, len(foods)):
        sum_food += (foods[i] - target)
    return sum_food

def search(start, end, foods, target):
    if start > end:
        return None
    mid = (start + end) // 2

    if foods[mid] <= target: # target이 크면 잘릴 수 있으니까 mid에서부터 잘린 값들을 더하면 된다. 
        return mid
    else: # 작으면 오른쪽 부분으로 이동 
        return search(mid + 1, end, foods, target)
    

        

def main():
    N, M = map(int, input().split())

    foods = list(map(int, input().split()))

    foods.sort()

    max_food = foods[len(foods) - 1] # 정렬 후, 제일 큰 값 

    answer = 0

    for number in range(0, max_food + 1):
        result = search(0, N - 1, foods, number)
        #print(result, number)
        if result != None:
            avail = get_remain(foods, result, number)
            #print(avail, number, M)
            if avail >= M:
                answer = number
    
    print(answer)
    


if __name__ ==  "__main__":
    main() 