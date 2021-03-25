import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    input_string = input().strip()
    input_string = list(input_string)
    
    stack = []
    while input_string:
        value = input_string.pop(0)
        if not stack:
            stack.append(value)
        else:
            if stack[-1] == '(' and value == ')':
                stack.pop()
            else:
                stack.append(value)
    if not stack:
        print("YES")
    else:
        print("NO")