# 더하기만 있으므로 연산자의 우선순위는 필요없다. 

def solve():
    n = int(input())
    e = input().strip()
    expression = list(e)

    post_expression = []
    operator_stack = []

    for v in expression: # 후위 표기법으로 변경 
        if v >= '0' and v <= '9':
            post_expression.append(v)

        else:
            if not operator_stack:
                operator_stack.append(v)
            else:
                while operator_stack:
                    node = operator_stack.pop()
                    post_expression.append(node)
                operator_stack.append(v)
    if operator_stack:
        post_expression.extend(operator_stack)
    
    stack = []

    for e in post_expression: # 계산 
        if e >= '0' and e <= '9':
            stack.append(e)
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(int(num1) + int(num2))
    
    #print(stack)
    return stack[0]
            


def main():
    #T = int(input())
    for i in range(10):
        result = solve()
        print("#" + str(i + 1), result)

if __name__ ==  "__main__":
    main()
