# 문제 이해는 되지만 
# 이를 어떻게 그래프 문제로 풀어야할지 감이 안와서 일단 그냥 풀어보았다,, 


def main():
    g = int(input()) # 탑승구 수 
    p = int(input()) # 비행기 수 

    graph = [[] for _ in range(g + 1)] # 탑승구 수만큼 그래프 생성 

    for i in range(1, g + 1):
        for j in range(i + 1, g + 1):
            graph[i].append(j)
    

    count = 0 
    for i in range(p):
        airplane = int(input())
        is_ok = False
        if not graph[airplane]: # 이미 도킹됨
            for j in range(airplane - 1, -1, -1):
                if graph[j]: # 차례로 뒤로 이동
                    graph[j] = []
                    is_ok = True
                    break 
        else: # 도킹 안된경우
            graph[airplane] = []
            is_ok = True
        
        if not is_ok:
            print(count)
            break
        count += 1


            



if __name__ ==  "__main__":
    main()