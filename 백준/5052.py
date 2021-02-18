# 문자열로 해서 정렬하면 
# 나 다음 문자열만 비교하면 되기 때문에
# 탐색하면서 나와 내 다음 문자열 비교했을 때 나로 다음 문자열이 시작하면
# return NO

import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    phone_list = []
    for _ in range(n):
        phone_number = input().strip()
        phone_list.append(phone_number)

    phone_list.sort()

    for i in range(n - 1):
        length = len(phone_list[i])
        if phone_list[i] == phone_list[i + 1][:length]:
            return 'NO'
    return 'YES'

def main():
    T = int(input())
    result = []
    for _ in range(T):
        answer = solve()
        result.append(answer)
        
    for r in result:
        print(r)
    

if __name__ ==  "__main__":
    main()