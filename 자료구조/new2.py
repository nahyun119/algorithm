def solution(program, flag_rules, commands):
    answer = []
    rules = {}
    
    for rule in flag_rules:
        tag, argument = rule.split()
        rules[tag] = argument 
    
    
    for i in range(len(commands)):
        temp = commands[i].split()
        stack = []
        flag = True
        # print(temp)
        for index, value in enumerate(temp):
            # print(index,value)
            # print(stack, value)
            if index == 0: # 프로그램 이름
                if value == program:
                    continue 
                else:
                    flag = False 
                    break 
            else:
                if not stack:
                    stack.append(value)
                else:
                    c = stack.pop()
                    if c not in rules:
                        flag = False 
                        break 
                    if rules[c] == 'NUMBER': # 0 ~ 9
                        # print(c, value, flag)
                        for k in value:
                            if k >= '0' and k <= '9':
                                continue 
                            else:
                                flag = False 
                                break
                        if not flag: # 명령어 검사 종료 
                            break 
                            
                    if rules[c] == 'STRING': # 알파벳 대소문자 
                        for k in value:
                            if (k >= 'a' and k <= 'z') or (k >= 'A' and k <= 'Z'):
                                continue
                            else:
                                flag = False 
                                break 
                        if not flag: # 명령어 검사 종료 
                            break 
                    if rules[c] == 'NULL': # 아무것도 안오니까 뒤에 명령어만 올 수 있다. 
                        # print(c, value, flag)
                        if value in rules:
                            stack.append(value) # 명령어가 바로오면 명령어를 넣는다. 
                            continue 
                        else:
                            flag = False 
                            break
        if stack:
            c = stack.pop()
            if c not in rules:
                flag = False
            elif rules[c] != 'NULL':
                flag = False
        
        answer.append(flag)
        
    return answer
["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"]
["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]