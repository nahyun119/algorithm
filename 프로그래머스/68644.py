
def solution(numbers):
    answer = []
    
    length = len(numbers)
    numbers.sort()
    
    ans = set()
    for i in range(length):
        for j in range(i + 1, length):
            ans.add(numbers[i] + numbers[j])
            
    answer = list(ans)
    answer.sort()
    return answer