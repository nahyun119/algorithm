def check(answer):
    
    for value in answer:
        is_ok = []
        for frame in answer:
            is_done = False
            print(value, frame)
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

def main():
    answer = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
    print(check_1(answer))
if __name__ ==  "__main__":
    main()