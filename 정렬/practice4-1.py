# 우선순위 큐는 원소를 넣었다 빼는 것만으로도 정렬된 결과를 얻을 수 있다.
import heapq

def main():
    N = int(input())

    number_list = []

    for i in range(N):
        heapq.heappush(number_list, int(input()))

    answer = 0 # 두 묶음씩 몇번을 비교했는지 총 비교 횟수 

    while len(number_list) > 1:
        first = heapq.heappop(number_list)
        second = heapq.heappop(number_list)

        total = first + second
        answer += total
        heapq.heappush(number_list, total)

    print(answer)

if __name__ ==  "__main__":
    main() 