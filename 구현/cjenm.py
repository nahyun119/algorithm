compressed = input().strip()

answer = ''
pa = ['(', ')']
stack = []

for i in compressed:
    if i == ')':
        string = ''
        while stack:
            t = stack.pop()
            if t == '(':
                break 
            else:
                string += t 
        
        number = ''
        while stack:
            t = stack.pop()
            if t not in '0123456789':
                stack.append(t)
                break 
            else:
                number += t 
        string = string[::-1]
        number = number[::-1]
        # print(string, number)
        new = string * int(number)
        if stack:
            stack.append(new[::-1])
        else:
            answer += new
        # print(answer)
    else:
        if not stack and i not in '0123456789' and i not in pa:
            answer += i
        else:
            stack.append(i)
    
    # print(stack)

print(answer)