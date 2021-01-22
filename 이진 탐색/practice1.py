# 이진 탐색을 통해서 해당 원소를 찾으면 count += 1을 한다.
# 이 때 해당 값이 여러 개 있을 수 있으므로 값을 찾으면 
# 양 옆으로 시작점, 끝점을 조정해서 다시 탐색하도록 하였다. 

count = 0
def binary_search(start, end, number_list, target):
    global count

    if start > end:
        return
    
    mid = (start + end) // 2

    if number_list[mid] == target: # 찾은 경우 
        count += 1
        binary_search(mid + 1, end, number_list, target) # 찾은 원소 양옆으로 이동해서 찾기 
        binary_search(start, mid - 1, number_list, target)
        return 

    if number_list[mid] > target:
        return binary_search(start, mid - 1, number_list, target)
    if number_list[mid] < target:
        return binary_search(mid + 1, end, number_list, target)
    

    

def main():
    N, X = map(int, input().split())

    number_list = list(map(int, input().split()))

    start = 0
    end = N - 1
    
    binary_search(start, end, number_list, X)

    if count == 0:
        print(-1)
        return
    print(count)
    

        

if __name__ ==  "__main__":
    main() 