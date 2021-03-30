numbers = list(map(int, input().split()))

def quick_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    # 피벗을 정하는 경우는 많다. 여기서는 맨 처음 원소를 피벗으로 정한다.
    pivot = unsorted_list[0]
    remain = unsorted_list[1:] # 피벗을 제외한 나머지 원소들

    left = [x for x in unsorted_list if x < pivot]
    right = [x for x in unsorted_list if x > pivot]

    print(left, right)
    return quick_sort(left) + [pivot] + quick_sort(right) # 퀵 정렬을 할 때마다 최소 하나의 원소를 자기 위치를 찾을 수 있다. pivot! 
print(quick_sort(numbers))