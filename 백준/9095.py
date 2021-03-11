import sys
input = sys.stdin.readline
T = int(input())
result = []
def add(number):
    global answer 
    if number == n:
        answer += 1
        return 
    if number > n:
        return 
    add(number + 1)
    add(number + 2)
    add(number + 3 )


for t in range(T):
    n = int(input())
    answer = 0  

    for i in range(1, 4):
        add(i)

    result.append(answer)
for r in result:
    print(r)