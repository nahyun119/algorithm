numbers = list(map(int, input().split()))

def merge(left, right):
    i = 0
    j = 0 

    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] > right[j]: # 비교해서 더 작은 애들 먼저 넣을 수 있도록 
            sorted_list.append(right[j])
            j += 1
        else:
            sorted_list.append(left[i])
            i += 1
    
    while i < len(left): # 작다면 왼쪽 남은 부분을 다 넣어준다.
        sorted_list.append(left[i])
        i += 1
    
    while j < len(right): # 작다면 오른쪽 남은 부분을 다 넣어준다.
        sorted_list.append(right[j])
        j += 1
    # print(left, right, sorted_list)
    return sorted_list



def mergesort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    mid = len(unsorted_list) // 2
    
    left = mergesort(unsorted_list[:mid])
    right = mergesort(unsorted_list[mid:])
    
    return merge(left, right)

print(mergesort(numbers))