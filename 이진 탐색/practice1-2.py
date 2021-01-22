# 파이썬 이진탐색 라이브러리인 bisect을 이용한 경우 

from bisect import bisect_right, bisect_left

def main():
    N, X = map(int, input().split())

    number_list = list(map(int, input().split()))

    left_index = bisect_left(number_list, X)
    right_index = bisect_right(number_list, X)

    count = right_index - left_index

    if count == 0:
        print(-1)
        return

    print(count)


if __name__ ==  "__main__":
    main() 