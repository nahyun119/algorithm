                        
        
        
#         for index, value in enumerate(temp):
#             print(flag_stack, argument_stack)
#             if index == 0: # 프로그램 검사
#                 if value == program:
#                     continue
#                 else:
#                     flag = False
#                     break 
#             else:
#                 if not flag_stack:
#                     if value in rules:
#                         flag_stack.append(value)
#                     else:
#                         flag = False # 명령어가 없는데 인자가 온 경우 검사 종료 
#                         break 
#                 else:
#                     if value in rules: # flag라면 이전 flag 처리 
#                         c = flag_stack.pop() 
#                         if rules[c] == 'NUMBER': # 숫자하나 
#                             if len(argument_stack) != 1:
#                                 flag = False 
#                                 break 
#                             else:
#                                 argument = argument_stack.pop()
#                                 if not is_number(argument):
#                                     flag = False
#                                     break 
                                    
#                         if rules[c] == 'NUMBERS':
#                             if not argument_stack: # 없으면 종료 
#                                 flag = False 
#                                 break 
#                             else:
#                                 while argument_stack:
#                                     a = argument_stack.pop()
#                                     if not is_number(a):
#                                         flag = False 
#                                         break 
#                                     else:
#                                         continue
#                                 if not flag:
#                                     break 
#                         if rules[c] == 'STRING':
#                             if len(argument_stack) != 1:
#                                 flag = False 
#                                 break 
#                             else:
#                                 argument = argument_stack.pop()
#                                 if not is_string(argument):
#                                     flag = False 
#                                     break 
#                         if rules[c] == 'STRINGS':
#                             if not argument_stack:
#                                 flag = False 
#                                 break 
#                             else:
#                                 while argument_stack:
#                                     a = argument_stack.pop()
#                                     if not is_string(a):
#                                         flag = False 
#                                         break
#                                     else:
#                                         continue 
#                                 if not flag:
#                                     break
#                         if rules[c] == 'NULL':
#                             if value in rules:
#                                 flag_stack.append(value) # 명령어가 바로오면 명령어를 넣는다. 
#                                 continue 
#                             else:
#                                 flag = False 
#                                 break  
#                         flag_stack.append(value)
#                     else: # 인자라면 인자를 받는다. 
#                         argument_stack.append(value)
                        
#         if flag_stack:
#             c = flag_stack.pop()
#             if rules[c] == 'NUMBER': # 숫자하나 
#                 if len(argument_stack) != 1:
#                     flag = False 
#                     break 
#                 else:
#                     argument = argument_stack.pop()
#                     if not is_number(argument):
#                         flag = False
#                         break 
                                    
#             if rules[c] == 'NUMBERS':
#                 if not argument_stack: # 없으면 종료 
#                     flag = False 
#                     break 
#                 else:
#                     while argument_stack:
#                         a = argument_stack.pop()
#                         if not is_number(a):
#                             flag = False 
#                             break 
#                         else:
#                             continue
#                             if not flag:
#                                 break 
#             if rules[c] == 'STRING':
#                 if len(argument_stack) != 1:
#                     flag = False 
#                     break 
#                 else:
#                     argument = argument_stack.pop()
#                     if not is_string(argument):
#                         flag = False 
#                         break 
#             if rules[c] == 'STRINGS':
#                 if not argument_stack:
#                     flag = False 
#                     break 
#                 else:
#                     while argument_stack:
#                         a = argument_stack.pop()
#                         if not is_string(a):
#                             flag = False 
#                             break
#                         else:
#                             continue 
#                     if not flag:
#                         break
#             if rules[c] == 'NULL':
#                             if value in rules:
#                                 flag_stack.append(value) # 명령어가 바로오면 명령어를 넣는다. 
#                                 continue 
#                             else:
#                                 flag = False 
#                                 break  
#                         flag_stack.append(value)
            