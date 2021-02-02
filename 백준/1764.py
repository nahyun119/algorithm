import sys

input = sys.stdin.readline # -> 속도 줄이려고 이렇게 했는데 내장함수 input 사용한거랑 20배 이상 차이가 난다.. 

def main():
    n, m = map(int, input().split())

    # target에 search가 있는지 이분탐색

    if n < m:
        search = []
        target = []
        for i in range(n):
            #search.append(str(input()))
            search.append(input().strip())
        
        for i in range(m):
            #target.append(str(input()))
            target.append(input().strip())

    else:
        search = []
        target = []
        for i in range(n):
            #target.append(str(input()))
            target.append(input().strip())
        
        for i in range(m):
            #search.append(str(input()))
            search.append(input().strip())


    target.sort() # 이름 정렬 
    length = len(target)
    result = []
    for name in search:
        start = 0
        end = length - 1
        while start <= end:
            mid = (start + end) // 2
            if target[mid] == name:
                result.append(name)
                break
            if target[mid] > name:
                end = mid - 1 # 왼쪽 범위로 이동
            else:
                start = mid + 1 # 오른쪽 범위로 이동 

    re_length = len(result)
    print(re_length)

    result.sort()
    for re in result:
        print(re)
            


if __name__ ==  "__main__":
    main()