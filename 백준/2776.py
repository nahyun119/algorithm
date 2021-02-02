import sys
input = sys.stdin.readline

def search():
    n = int(input()) 
    search = list(map(int, input().split())) # 수첩 1
    m = int(input())
    targets = list(map(int, input().split())) # 수첩 2

    search.sort()

    #result = []
    for target in targets:
        start = 0
        end = n - 1 # 제일 최댓값
        is_in = False 
        while start <= end:
            mid = (start + end) // 2

            if search[mid] == target:
                is_in = True
                break
            
            if search[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        if is_in:
            print(1)
        else:
            print(0)



def main():
    T = int(input())

    for _ in range(T):
        search()


if __name__ ==  "__main__":
    main()