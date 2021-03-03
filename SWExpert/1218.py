def solve():
    n = int(input())
    test = list(input().strip())
    stack = []
    #print(test, len(test))
    path = [['<', '>'], ['(', ')'], ['[', ']'], ['{', '}']]

    for i in range(n):
        value = test[i]
        print(stack, value)
        if not stack:
            stack.append(value)
        else:
            is_done = False 
            for i in range(4):
                if value in path[i] and stack[-1] in path[i]:
                    if value != stack[-1]:
                        is_done = True 
                        break 
            if is_done:
                stack.pop()
            else:
                stack.append(value)

    if stack:
        return 0
    else:
        return 1      

def main():
    for i in range(10):
        result = solve()
        print("#" + str(i + 1), result)
                    
            

if __name__ ==  "__main__":
    main()