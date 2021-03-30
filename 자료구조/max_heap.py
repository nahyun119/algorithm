max_heap = [-1] # root가 인덱스 1부터 시작할 수 있도록 
heapsize = 0

def insert_max_heap(data):
    global max_heap, heapsize 
    heapsize += 1
    max_heap.append(data)
    
    for i in range(heapsize, 1, -1):
        if max_heap[i] > max_heap[i // 2]: # 부모보다 자식이 더 크면
            max_heap[i // 2], max_heap[i] = max_heap[i], max_heap[i // 2]
        else:
            break 
insert_max_heap(1)
print(max_heap)
insert_max_heap(2)
print(max_heap)
insert_max_heap(4)
print(max_heap)
insert_max_heap(3)
print(max_heap)

def delete_max_heap():
    global maxheap, heapsize
    if heapsize == 0:
        return 0
    data = max_heap[1]
    max_heap[1] = max_heap[heapsize] # 마지막 노드를 루트로 이동 
    max_heap[heapsize] = 0  # 마지막 노드 초기화
    heapsize -= 1
    print(data)
    i =  1
    while i * 2 <= heapsize:
        if max_heap[i] > max_heap[i * 2 + 1] and max_heap[i] > max_heap[i * 2]: # 부모가 자식들보다 크면 
            break
        elif max_heap[i * 2] > max_heap[i * 2 + 1]: # 왼쪽 자식이 더 큰 경우 왼쪽 자식이랑 부모랑 변경 
            max_heap[i], max_heap[i * 2] = max_heap[i * 2], max_heap[i]
            i = i * 2
        elif max_heap[i * 2 + 1] > max_heap[i * 2]: # 오른쪽 자식이 더 큰 경우 오른쪽 자식이랑 부모랑 변경 
            max_heap[i * 2 + 1], max_heap[i] = max_heap[i], max_heap[i * 2 + 1]

    return data

delete_max_heap()
print(max_heap)



