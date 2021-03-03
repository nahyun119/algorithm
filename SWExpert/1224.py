# 후위 표기 방법 
# 후위 계산식 계산 
def solve():
    n = int(input())
    expression = list(input().strip())

    hash_map = {} # 우선순위 
    hash_map['+'] = 2
    hash_map['*'] = 3
    hash_map['('] = 1
    hash_map[')'] = 1 

    ### 후위 표기 방법 
 
    post_expression = []
    operator_stack = []

    for e in expression:
        if e >= '0' and e <= '9':
            post_expression.append(e)
        else:
            if e == '(':
                operator_stack.append(e)
            elif e == ')':
                while True:
                    value = operator_stack.pop()
                    if value == '(':
                        break
                    else:
                        post_expression.append(value)
            elif e == '*' or e == '+':
                priority1 = hash_map[e]
                if not operator_stack:
                    operator_stack.append(e)
                else:
                    while operator_stack:
                        value = operator_stack.pop()
                        priority2 = hash_map[value]
                        if priority1 > priority2:
                            operator_stack.append(value)
                            operator_stack.append(e)
                            break
                        else:
                            post_expression.append(value)
                    if not operator_stack: # 아무것도 없는 경우, 우선순위가 다 높은 것만 있는 경우 현재 연산자를 append 
                        operator_stack.append(e)
     
    if operator_stack:
        post_expression.extend(operator_stack)


    # 후위 표기식 계산 
    stack = []
    for e in post_expression:
        #print(stack)
        if e == '+':
            num1 = stack.pop()
            num2 = stack.pop()
            value = num1 + num2
            stack.append(value)
        elif e == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            value = num1 * num2
            stack.append(value)
        elif e >= '0' and e <= '9':
            stack.append(int(e))
    
    return stack[0]




def main():
    for i in range(10):
        result = solve()
        print("#" + str(i + 1), result)


if __name__ ==  "__main__":
    main()