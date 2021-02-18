# 파이썬에서 반올림은 round() 내장함수 사용 
# 시간초과 
# -> 입력받는 부분에서 문제가 생긴 듯 하다 ..
# -> 내장함수 input() 말고 sys.stdin.readline 사용하니까 바로 통과

import sys

input = sys.stdin.readline

def main():
    n = int(input())

    numbers = []
    hash_map = {}
    total = 0

    for _ in range(n):
        number = int(input())
        total += number
        numbers.append(number)
        if number in hash_map:
            hash_map[number] += 1
        else:
            hash_map[number] = 1
    
    numbers.sort()
    s_map = sorted(hash_map.items(), key = lambda x : (-x[1], x[0]))
    
    print(round(total / n))
    print(numbers[n // 2])
    
    if len(s_map) > 1 and s_map[0][1] == s_map[1][1]: # 최빈값이 동일하면 
        print(s_map[1][0])
    else:
        print(s_map[0][0])

    print(numbers[-1] - numbers[0])

    # print(numbers)
    # print(s_map)
    


if __name__ ==  "__main__":
    main()