import sys 
n, k = map(int, input().split())
l_list = []
for i in range(1, n + 1):
    l_list.append(i)



length = len(l_list)
current = (k - 1) % length 
# print(l_list)
result = []
while len(l_list) != 0:
    data = l_list.pop(current)
    length = len(l_list)
    if length == 0:
        break
    current = (current + k - 1) % length
    result.append(data)
    
result.append(data)
print("<", end = '')
for r in range(n):
    if r == n - 1:
        print(result[r], end = "")
    else:
        print(result[r], end = ", ")
print(">")
