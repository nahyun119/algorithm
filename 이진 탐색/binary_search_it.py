# 반복문을 이용한 binary search
def main():
    N, target = list(map(int, input().split()))

    array = list(map(int, input().split()))

    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            print(mid + 1)
            return  
        if array[mid] < target: # target이 더 큰 경우 start 변경
            start = mid + 1
        if array[mid] > target: # target이 더 작은 경우 end 변경 
            end = mid - 1
        
    print("결과가 없다.")
    return 



if __name__ ==  "__main__":
    main() 