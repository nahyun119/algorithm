import sys
input = sys.stdin.readline

n = int(input())
file_map = {}
for i in range(n):
    name, ext = input().strip().split('.')
    if ext in file_map:
        file_map[ext] += 1
    else:
        file_map[ext] = 1

temp = []
for i in file_map:
    temp.append((i, file_map[i]))

temp.sort()
for i in temp:
    print(i[0], i[1])