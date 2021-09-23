import sys 
input = sys.stdin.readline 

n = int(input())
numbers = list(map(int, input().split()))
p, m, mu, d = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈 

# -10억 ~ 10억 
min_answer = 1000000000
max_answer = -1000000000

def dfs(order, value, plus, minus, mul, div):
    global min_answer, max_answer
    #print(order, value, plus, minus, mul, div)
    if plus + minus + mul + div == 0 or order > n + 1: # 다 쓴 경우 
        min_answer = min(value, min_answer)
        max_answer = max(value, max_answer)
        return 
    if plus > 0:
        dfs(order + 1, value + numbers[order], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(order + 1, value - numbers[order], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(order + 1, value * numbers[order], plus, minus, mul - 1, div)
    if div > 0:
        temp = -1 * value if value < 0 else value 
        temp = temp // numbers[order]
        dfs(order + 1, -1 * temp if value < 0 else temp, plus, minus, mul, div - 1)      

dfs(1, numbers[0], p, m, mu, d)

print(max_answer)
print(min_answer)


    