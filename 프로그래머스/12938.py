# 맨처음에는 heapq 이용해서 q를 s // n 값으로 n 개 넣어서
# 합이 s가 될때까지 돌렸는데 정확성 테스트는 통과하지만 효율성 테스트에서 시간초과가 발생하였다
# 그래서 O(n)으로 구현하기 위해서 q에 먼저 s // n 값을 넣고 s 를 s // n을 뺀 값으로, n을 n - 1로 초기화
# 그리고 이 과정을 계속 반복함 n번만큼
# 곱이 최대가 되려면 값이 고르게? 큰 편차없이 있어야하기 때문에 s // n을 넣음 

import heapq
def solution(n, s):
    answer = []
    
    if n == 1 and s == 1:
        return [1]
    elif n > s:
        return [-1]
    
    q = [s // n]
    s -= s // n
    n -= 1
#     while sum(q) < s:
#         num = heapq.heappop(q)
#         num += 1
#         heapq.heappush(q, num)
    
#     answer = sorted(q)
    for i in range(n, 1, -1):
        q.append(s // i)
        s -= s // i
    q.append(s)
    
    answer = sorted(q)
    
    return answer