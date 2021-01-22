# 중간값을 찾으려고 하는 값이라고 생각
# 중간값이 가리키는 값 < 중간값: 오른쪽 부분 탐색
# 중간값이 가리키는 값 > 중간값: 왼쪽 부분 탐색 

def binary_search(start, end, number_list):
    #print(start, end)
    length = len(number_list)

    if start > end:
        return None
    
    mid = (start + end) // 2

    if mid == number_list[mid]:
        return mid

    if mid < number_list[mid]:
        return binary_search(start, mid - 1, number_list)
    else:  # mid > number_list[mid]
        return binary_search(mid + 1, end, number_list)




def main():
    N = int(input())

    number_list = list(map(int, input().split()))

    #number_list.sort()

    start = 0
    end = N - 1

    result = binary_search(start, end, number_list)

    if result == None:
        print(-1)
        return
    print(result)


    



        

if __name__ ==  "__main__":
    main() 