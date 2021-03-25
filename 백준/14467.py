import sys
input = sys.stdin.readline 
n = int(input())
cow_map = {}
result = 0
for i in range(n):
    number, location = map(int, input().split())
    if number not in cow_map:
        cow_map[number] = location
    else:
        if cow_map[number] != location:
            result += 1
        cow_map[number] = location
print(result)