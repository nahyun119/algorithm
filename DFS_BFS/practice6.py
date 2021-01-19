from itertools import combinations

def check(teachers, students, walls): # 장애물을 설치한 후 막을 수 있는지 
    for teacher in teachers:
        is_done = []
        for student in students:
            #print(teacher, student)
            row_ok = False
            col_ok = False
            if teacher[1] == student[1]: # 선생님과 학생이 같은 열 
                for wall in walls:
                    if wall[1] == student[1]:
                        if (student[0] < wall[0] and wall[0] < teacher[0]) or (student[0] > wall[0] and wall[0] > teacher[0]): # 장애물이 막을 수 있는지 확인 
                            row_ok = True
                            break 
            else:
                row_ok = True
            if teacher[0] == student[0]: # 선생님과 학생이 같은 행
                for wall in walls:
                    if wall[0] == student[0]:
                        if (student[1] < wall[1] and wall[1] < teacher[1]) or (student[1] > wall[1] and wall[1] > teacher[1]): # 장애물이 막을 수 있는지 확인 
                            col_ok = True
                            break 
            else:
                col_ok = True
            #print(row_ok, col_ok)
            is_done.append(row_ok & col_ok)  
        if False in is_done: # 실패한 경우가 있으면 
            return False
    return True



def main():
    N = int(input())

    graph = []

    for i in range(N):
        graph.append(list(map(str, input().split())))

    teachers = []
    walls = []
    students = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'T': 
                teachers.append((i, j)) # 선생님이 있는 자리 
            if graph[i][j] == 'X':
                walls.append((i, j)) # 장애물을 세울 수 있는 자리 
            if graph[i][j] == 'S':
                students.append((i, j))

    item = []
    for i in range(len(walls)):
        item.append(i)
    

    avail = list(combinations(item, 3)) # 장애물을 세울 수 있는 조합 
    
    
    for i, j, k in avail:
        # 가능한 장애물 조합 가져오기 
        list_o = []
        list_o.append(walls[i])
        list_o.append(walls[j])
        list_o.append(walls[k])
        # first = walls[i]
        # second = walls[j]
        # third = walls[k]
        if check(teachers, students, list_o):
            print("YES")
            return
    print("NO")




if __name__ ==  "__main__":
    main()