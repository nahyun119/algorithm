import sys
input = sys.stdin.readline

# 메모리초과가 발생해서
# 약수 갯수를 담는 배열을 hash_map으로 변경하여 진행
# 그랬더니 시간초과 
# 그래서 while 문 안에서 말고 밖에서 미리 먼저 약수 갯수 다 구해놓고 진행해보기로 이게 더 시간이 덜 걸림 

# 아직도 시간초과 ㅠㅠㅠㅠ

def main():
    n = int(input())
    k = int(input())

    start = 1
    end = n * n
    
    answer = 0
    hash_map = {}
    
    # for j in range(1, end + 1):
    #     c = 0
    #     if j not in hash_map:
    #         for i in range(1, n + 1):
    #             d = j % i 
    #             q = j // i
    #             if d == 0 and q <= n:
    #                 c += 1
    #         hash_map[j] = c

    # for i in range(1, end + 1):
    #     temp = 0
    #     for j in range(1, n + 1):
    #         temp += min(i // j, n)
    #     hash_map[i] = temp
    # print(hash_map)

    result = 0

    while start <= end:
        mid = (start + end) // 2
        
        temp = 0
        for i in range(1, n + 1): # -> 이렇게 하면 훨씬 더 쉽게 구할 수 있다.. 
            temp += min(mid // i, n) # mid 이하의 i의 배수, 최대 N

        #count = sum(hash_map[i] for i in range(1, mid + 1))

        # if count >= k and k > count - hash_map[mid] and hash_map[mid] != 0:
        #     result = mid 
        #     break
        # if count == k and hash_map[mid] == 0:
        #     end = mid - 1
        if temp >= k:
            result = mid
            end = mid - 1
        elif temp < k:
            start = mid + 1

    print(result)



if __name__ ==  "__main__":
    main()