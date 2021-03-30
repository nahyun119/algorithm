numbers = list(map(int, input().split()))

def heapsort(unsorted_list):
    n = len(unsorted_list)
    # max heap 초기화 
    for i in range((n // 2) - 1, -1, -1):
        heapify(unsorted_list, n, i)
    
    for i in range(n - 1, 0, -1):
        unsorted_list[0], unsorted_list[i] = unsorted_list[i], unsorted_list[0] # 하나씩 변경 
        heapify(unsorted_list, i, 0) # 변경한 후 다시 max heap 만든다. 
    


def heapify(unsorted_list, n, i):
    parent = i # 부모 노드
    left_child = i * 2 + 1 # 왼쪽 자식 
    right_child = i * 2 + 2 # 오른쪽 자식 
    print(unsorted_list)


    # 왼쪽 자식이 부모 노드 보다 큰 경우 부모랑 자식이랑 변경 
    # 이 때 n보다 작다 조건을 넣어서 루트랑 마지막 값이랑 변경한 경우는 건들지 않도록 
    if left_child < n and unsorted_list[parent] < unsorted_list[left_child]:
        parent = left_child

    if right_child < n and unsorted_list[parent] < unsorted_list[right_child]:
        parent = right_child
    
    if i != parent: # 부모 값이 변경되었다면 
        unsorted_list[parent], unsorted_list[i] = unsorted_list[i], unsorted_list[parent] # 값 변경 
        heapify(unsorted_list, n, parent)

heapsort(numbers)
         

