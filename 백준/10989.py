# 숫자 갯수는 천만개이지만
# n의 범위가 10000이므로 
# 10001 크기의 리스트를 하나만들어서 계수정렬을 진행하면 된다!!!!! 
# 정수이고 범위가 갯수보다 작고(100만이하) 그리고 중복이 되는 경우 계수정렬을 이용하면 된다 O(N + K) 데이터 수 + 최대 값 

import sys

input = sys.stdin.readline

def main():
    n = int(input())

    numbers = [0] * 10001
    for _ in range(n):
        number = int(input())
        numbers[number] += 1
    
    for index, number in enumerate(numbers):
        for i in range(number):
            print(index)
    

if __name__ ==  "__main__":
    main()