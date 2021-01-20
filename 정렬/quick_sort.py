def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료 
        return
    pivot = start # 피벗의 첫번째 원소 
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right : # 범위를 벗어난 경우, 오른쪽 데이터랑 피벗이랑 자리 변경
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않으면 큰 데이터랑 작은 데이터랑 자리 변경
            array[left], array[right] = array[right], array[left]
        
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)



def main():
    num = list(map(int, input().split()))

    quick_sort(num, 0, len(num) - 1)
    print(num)

if __name__ ==  "__main__":
    main()  