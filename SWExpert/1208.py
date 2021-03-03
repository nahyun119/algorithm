import heapq

def get_max(q):
    queue = []
    max_value = 0
    while q:
        box = heapq.heappop(q)
        if q: # 마지막 값이 아니므로 
            heapq.heappush(queue, box)
        else: # 마지막 값 
            max_value = box 
    
    return max_value, queue




def solve():
    n = int(input())
    boxes = list(map(int, input().split()))
    q = []
    for i in range(len(boxes)):
        heapq.heappush(q, boxes[i])

    
    for i in range(n):
        min_value = heapq.heappop(q)
        max_value, q = get_max(q)
        if max_value - min_value <= 1:
            return max_value - min_value
        else:
            min_value += 1
            max_value -= 1
            heapq.heappush(q, min_value)
            heapq.heappush(q, max_value)

    min_value = heapq.heappop(q)
    max_value, q = get_max(q) 
    return max_value - min_value
    



def main():
    for i in range(10):
        result = solve()
        print("#" + str(i + 1), result)
    # result= solve()
    # print(result)
if __name__ ==  "__main__":
    main()