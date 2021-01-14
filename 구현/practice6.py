def check(answer):
    
    for value in answer:
        is_ok = []
        for frame in answer:
            if value != frame: # 자기 자신이 아닌 경우
                if value[2] == 0: # 기둥인 경우
                    if value[1] == 0:
                        is_ok.append(True)
                    if frame[2] == 1 and ([frame[0], frame[1]] == [value[0], value[1]] or [frame[0]+1, frame[1]] == [value[0], value[1]]):
                        is_ok.append(True)
                    if frame[2] == 0 and ([frame[0], fream[1] + 1] == [value[0], value[1]]):
                        is_ok.append(True)
                if value[2] == 1: # 보인 경우
                    if frame[2] == 0 and ([value[0], value[1]] == [frame[0], frame[1] + 1] or [value[0] + 1, value[1]] == [frame[0], frame[1] + 1]):
                        is_ok.append(True)
                    if [value[0] -1, value[1], 1] in answer and [value[0] + 1, value[1], 0] in answer:
                        is_ok.append(True)
        if not is_ok:
            return False
    return True
                    
                        
                            

def solution(n, build_frame):
    answer = []
    
    build = [[0] * (n + 1) for _ in range(n + 1)]
    
    while build_frame:
        frame = build_frame.pop(0)
        print(frame,answer)
        x = frame[0]
        y = frame[1]
        a = frame[2]
        b = frame[3]
        if b == 1: # 설치
            if a == 0: # 기둥
                if y == 0: # 바닥인 경우
                    build[x][y] = 1
                    build[x][y + 1] = 1
                    # build_frame.pop(0) # 작업했으므로 삭제 
                    answer.append([x,y,a])
                else:
                    if build[x][y] >= 1:
                        build[x][y] = 1
                        build[x][y + 1] = 1
                        # build_frame.pop(0) 
                        answer.append([x,y,a])
                    else:
                        if not build_frame: # 하나 남았는데 작업이 안되는 경우 종료 
                            return answer
                        build_frame.append(frame) # 작업이 안된 경우 다시 넣기 
            if a == 1: # 보인 경우
                if build[x][y] >= 1:
                    build[x][y] = 1
                    build[x + 1][y] = 1
                    answer.append([x,y,a])
                else:
                    if not build_frame: # 하나만 남았는데 작업이 안되는 경우 종료 
                        return answer 
                    build_frame.append(frame) # 작업이 안된 경우 다시 넣기 
        else: # 삭제인 경우
            if a == 0: # 기둥인 경우
                print(build[x][y], build[x][y+1])
                build[x][y] -= 1
                build[x][y + 1] -= 1
                if y == 0: # 바닥인 경우 
                    if build[x][y + 1] <= 0:
                        build[x][y] += 1
                        build[x][y + 1] +=1
                    else: # 삭제 가능한 경우 
                        print([x,y,a])
                        answer.remove([x,y,a])
                else:
                    if build[x][y] <= 0 or build[x][y + 1] <= 0: # 삭제 후 유지 안되면 
                        build[x][y] += 1
                        build[x][y + 1] +=1
                        #build_frame.pop(0)
                    else: # 삭제 가능한 경우 
                        print([x,y,a])
                        answer.remove([x,y,a])
            else: # 보인 경우
                print(x, y, a, build[x][y], build[x + 1][y])
                build[x][y] -= 1
                build[x + 1][y] -= 1
                if build[x][y] <= 0 or build[x + 1][y] <= 0 : # 삭제 후 유지 안되면 
                    build[x][y] += 1
                    build[x][y + 1] +=1
                    #build_frame.pop(0)
                else: # 삭제 가능한 경우 
                    print([x,y,a])
                    answer.remove([x,y,a])       
    answer.sort()
    print(answer)
    
    return answer