# 최소가 되어야하므로 -가 나온 후 다시 -가 나올 때까지 괄호를 쳐서 빼는 수를 크게 만든다. 

def main():
    expression = str(input())

    exp = [] # 숫자랑 연산이랑 분리해서 넣는 리스트 

    number = ""
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-':
            exp.append(int(number))
            exp.append(expression[i])
            number = ""
        else:
            number += expression[i]
    exp.append(int(number))
    
    #print(exp)

    result = exp[0]
    number = 0
    is_start = False
    for i in range(1, len(exp)):
        #print(number)
        if exp[i] == '-':
            if not is_start: # 괄호 시작 안했는데, - 나온 경우 괄호 시작 
                is_start = True
            else: # 괄호 시작 했는데 - 나온 경우 
                is_start = False # 괄호 끝
                result -= number # 괄호 안에 숫자 더한거 빼기 
                number = 0 # 숫자 초기화 
                is_start = True # - 다시 나와서 다시 괄호 시작 
        elif exp[i] == '+':
            continue
        else: # 숫자인 경우 
            if is_start: # 괄호인 경우 
                number += exp[i] # 괄호 내 숫자에 더한다 
            if not is_start and exp[i - 1] == '+': # 그냥 더하기인 경우
                result += exp[i] # 더한다 

    if is_start: # 괄호가 있는 경우, 괄호 안에 더한 숫자들을 뺀다 
        result -= number

    print(result)   



            

if __name__ ==  "__main__":
    main()