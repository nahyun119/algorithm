# 건물 조건에 부합하는지 확인하는 함수를 구현
# 함수를 구현한 후 삽입하거나 삭제할 때마다 부합하는지 확인하고
# 부합하지 않으면 해당 작업을 무시하도록 한다. 


# -> 건물 조건에 맞는지를 확인하는 작업을 구현하는 것이 까다롭다.
 
 def check(answer):
    if len(answer) == 1:
        return True
    for value in answer:
        is_ok = []
        for frame in answer:
            is_done = False
            if value != frame: # 자기 자신이 아닌 경우
                if value[2] == 0: # 기둥인 경우
                    if value[1] == 0:
                        is_done = True
                        is_ok.append(True)
                    if frame[2] == 1 and ([frame[0], frame[1]] == [value[0], value[1]] or [frame[0]+1, frame[1]] == [value[0], value[1]]):
                        is_done = True
                        is_ok.append(True)
                    if frame[2] == 0 and ([frame[0], frame[1] + 1] == [value[0], value[1]]):
                        is_done = True
                        is_ok.append(True)
                if value[2] == 1: # 보인 경우
                    if frame[2] == 0 and ([value[0], value[1]] == [frame[0], frame[1] + 1] or [value[0] + 1, value[1]] == [frame[0], frame[1] + 1]):
                        is_done = True
                        is_ok.append(True)
                    if [value[0] -1, value[1], 1] in answer and [value[0] + 1, value[1], 1] in answer:
                        is_done = True
                        is_ok.append(True)
            if is_done:
                break
        if not is_ok:
            return False
    return True
                    
                        
def check_1(answer):
    for value in answer:
        if value[2] == 0: # 기둥인 경우
            if value[1] == 0 or [value[0], value[1], 1] in answer or [value[0] - 1, value[1], 1] in answer or [value[0], value[1] - 1, 0] in answer:
                continue
            return False
        if value[2] == 1:
            if [value[0], value[1] - 1, 0] in answer or [value[0] + 1, value[1] - 1, 0] in answer or ([value[0] - 1, value[1], 1] in answer and [value[0] + 1, value[1], 1] in answer):
                continue
            return False
    return True                     

def solution(n, build_frame):
    answer = []
    
    while build_frame:
        frame = build_frame.pop(0)
        x = frame[0]
        y = frame[1]
        a = frame[2]
        b = frame[3]
        if b == 1: # 설치
            answer.append([x, y, a])
            if check_1(answer) == False:
                answer.remove([x, y, a]) 
        else: # 삭제인 경우
            answer.remove([x, y, a])
            if check_1(answer) == False: # 삭제 시 건물 조건에 부합하지 않는 경우
                answer.append([x, y, a])    
               
    answer.sort()
    #print(answer)
    return answer