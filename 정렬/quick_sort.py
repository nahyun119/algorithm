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
        # vl

def main():
    num = list(map(int, input().split()))

    

if __name__ ==  "__main__":
    main()  