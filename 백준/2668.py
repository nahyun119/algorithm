import sys
input = sys.stdin.readline 
n = int(input()) # numbers는 key, 

temp_map = {}
temp = []
for i in range(n): # temp는 value 
    value = int(input())
    temp_map[i + 1] = value
    temp.append(value)

result = []

visited = [0] * n 

# numbers에 있는 애들이 temp에 없으면 제거 이런 식으로 진행 
numbers = set([x for x in range(1, n + 1)])


diff = numbers - set(temp)
while len(diff) > 0:
    # print(numbers, temp)
    for i in diff:
        numbers.remove(i)
        del temp_map[i]
        
    temp = [temp_map[x] for x in temp_map]
    diff = numbers - set(temp)
    # print(numbers, temp, diff)
    

print(len(numbers))
for i in numbers:
    print(i)