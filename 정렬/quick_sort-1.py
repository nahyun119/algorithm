## 좀 더 직관적인 퀵 소트 
## 피벗을 기준으로 왼쪽은 피벗보다 작은 애들
## 피벗을 기준으로 오른쪽은 피벗보다 큰 애들 
## 피벗을 중심으로 정렬한 후에 다시 왼쪽, 오른쪽 나눠서 정렬을 한다. 
def quick_sort(num):
    if len(num) <= 1: # 원소 하나만 가진 경우 종료 
        return 
    
    pivot = num[0]
    tail = num[1:] # 피벗을 제외한 나머지

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분 

    return quick_sort(left_side) + pivot + quick_sort(right_side) # 왼쪽 부분 정렬 + 피벗 + 오른쪽 부분 정렬 




def main():
    num = list(map(int, input().split()))



if __name__ ==  "__main__":
    main()  