import heapq

def solution(nums):
    answer = 0
    
    n = len(nums)
    
    s_nums = set(nums) # 중복 제거 
    
    q = []
    
#     for i in s_nums: -> 갯수를 일일이 계산했는데, 생각해보니 그럴 필요가 없다 그냥 중복 없애면 된다.. 
#         n_count = nums.count(i)
#         if n_count != 0:
#             heapq.heappush(q, ((-1) * nums.count(i), i))
            
    
    count = min(len(s_nums), n // 2)

    answer = count
    return answer