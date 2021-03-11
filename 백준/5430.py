# 뒤집는게 계속 들어오면 시간초과 발생 
import sys
input = sys.stdin.readline
T = int(input())
result = []
for t in range(T):
    order = input().strip()
    order = order.replace('RR','') # 중복되는걸 줄여준다 
    order = list(order)
    n = int(input())

    numbers = input().strip()
    numbers = numbers[1:- 1]
    numbers = numbers.split(',')

    is_reversed = False
    left, right = 0, 0
 
    for i in range(len(order)):
        #print(numbers, hash_map)
        if order[i] == 'R':
            is_reversed = not is_reversed
        if order[i] == 'D':
            if not is_reversed: # 뒤집힌 상태가 아니라면 왼쪽을 줄인다
                left += 1
            else: # 뒤집힌 상태라면 오른쪽을 줄인다.
                right += 1

    if left + right <= n: # 줄이려는 숫자가 숫자 갯수보다 작거나 같아야
        numbers = numbers[left: n - right]
        if is_reversed: # 뒤집어야한다면?
            answer = "[" + ','.join(numbers[::-1]) + "]"
        else:
            answer = "[" + ','.join(numbers) + "]"
    else:
        answer = "error"
        
    result.append(answer)

for r in result:
    print(r)