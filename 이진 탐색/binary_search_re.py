# 재귀 방법을 이용한 binary search 
def binary_search(start, end, target, array):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    if array[mid] < target: # target이 중간 값보다 큰 경우
        start = mid + 1 # 탐색 범위의 시작을 중간 값보다 뒤 
        return binary_search(start, end, target, array)
    if array[mid] > target: # target이 중간 값보다 작은 경우
        end = mid - 1 # 탐색 범위의 끝을 중간 값 바로 앞 
        return binary_search(start, end, target, array)
    



def main():
    N, target = list(map(int, input().split()))

    array = list(map(int, input().split()))

    array.sort()

    result = binary_search(0, N - 1, target, array)
    if result == None:
        print("결과가 없다.")
    else: 
        print(result + 1) # 인덱스가 0부터 시작하므로 
    



if __name__ ==  "__main__":
    main()   