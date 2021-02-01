from bisect import bisect_left
from bisect import bisect_right 


def main():
    n = int(input())
    cards = list(map(int, input().split())) # 상근이가 가지고 있는 카드 리스트 
    m = int(input())
    mine = list(map(int, input().split())) # 몇 개를 가지고 있는지 알아내야하는 리스트 

    result = []
    cards.sort() # 이진 탐색하려면 정렬해야 

    for i in range(m):
        start = bisect_left(cards, mine[i])
        end = bisect_right(cards, mine[i])
        #print(start, end)
        result.append(end - start)

    print(*result)

if __name__ ==  "__main__":
    main()