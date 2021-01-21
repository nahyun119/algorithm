def search(start, end, products, target):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if products[mid] == target:
        return mid
    if products[mid] > target:
        return search(start, mid - 1, products, target)
    if products[mid] < target:
        return search(mid + 1, end, products, target)
    

def main():
    N  = int(input())
    products = list(map(int, input().split()))

    # 이진 탐색의 경우, 탐색하고자 하는 대상이 정렬되어야한다. 
    products.sort()

    M = int(input())
    needs = list(map(int, input().split()))

    for value in needs:
        result = search(0, N - 1, products, value)
        if result == None:
            print("No", end = " ")
        else:
            print("Yes", end = " ")




if __name__ ==  "__main__":
    main()   