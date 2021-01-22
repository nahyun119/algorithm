# 찾으려고 하는 값의 맨 처음 인덱스를 구하는 이진 탐색
# 찾으려고 하는 값의 맨 마지막 인덱스를 구하는 이진 탐색
# 두 개의 이진 탐색 함수를 이용해서 원소의 갯수를 구하는 방법

def first_index(start, end, number_list, target): # 첫번째 인덱슬르 찾는 이진 탐색 
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == 0 or target > number_list[mid - 1]) and number_list[mid] == target: # target이랑 중간 값이 동일, mid = 0 이거나 해당 값이 시작되는 맨 처음인 경우 
        return mid 
    elif number_list[mid] >= target: # 중간 값이 이상인 경우 끝점을 이동 
        return first_index(start, mid - 1, number_list, target)
    else: # 중간 값이 작은 경우 시작점을 이동
        return first_index(mid + 1, end, number_list, target)

def last_index(start, end, number_list, target):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == len(number_list) - 1 or number_list[mid + 1] > target) and number_list[mid] == target: # target이랑 같은 값이면서 제일 마지막이거나 중간 값 다음 값이 target보다 큰 경우 
        return mid
    elif number_list[mid] > target: # 미만인 경우 끝 점 이동 
        return last_index(start, mid - 1, number_list, target)
    else: # 중간 값 이상인 경우
        return last_index(mid + 1, end, number_list, target)
    
    






def main():
    N, X = map(int, input().split())

    number_list = list(map(int, input().split()))

    start = 0
    end = N - 1
    
    first = first_index(start, end, number_list, X)
    if first == None:
        print(-1) # 값이 없으므로 -1 출력 종료
        return 
    
    
    last = last_index(start, end, number_list, X)
    
    #print(first, last)
    count = last - first + 1

    if count == 0:
        print(-1)
        return

    print(count)


if __name__ ==  "__main__":
    main() 