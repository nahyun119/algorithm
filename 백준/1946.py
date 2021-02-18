import sys
input = sys.stdin.readline

# 먼저 첫번째 순위를 기준으로 정렬을 한 후, 반복문을 통해서 탐색을 한다.
# 맨처음 값을 mx, my로 두고 
# 그 다음 값이 mx < x, my < y라면 자기보다 둘 다 높은 사람이 있다는 것이고, 
# 자기 이전 사람이랑 비교했을 때(x는 오름차순 정렬이라 이미 x는 크고) y가 자기가 더 크면 2 3 3 5 이런 식이면 
# 합격을 못하기 때문에 
# 그리고 my > y 라면 그 값으로 업데이트 한다. y를 탐색한 것 중에서 제일 작은 값으로 업데이트 

def solve():
    n = int(input())
    grades = []
    
    for _ in range(n):
        a, b = map(int, input().split())
        #heapq.heappush(grades, (-1 * a, b))
        grades.append((a,b))
    
    grades.sort()
    #print(grades)

    # 시간복잡도를 줄여보자 
    count = n

    mx = grades[0][0]
    my = grades[0][1]

    for i in range(1, len(grades)):
        x = grades[i][0]
        y = grades[i][1]
        #print(x, y, mx, my, count)
        if (y > my and x > mx) or y > grades[i - 1][1]:
            count -= 1
        if y < my:
            mx = x
            my = y

    #print(count)


    # while True:
    #     #print(grades)
    #     is_done = False 
    #     for i in range(len(grades) - 1):
    #         x = grades[i][0]
    #         y = grades[i][1]
    #         print(grades, i, i + 1, grades[i + 1][1])
    #         if y < grades[i + 1][1]:
    #             #heapq.heappop(grades)
    #             grades.pop(i + 1)
    #             is_done = True
    #             break
    #     if not is_done:
    #         break
    
    return count 
    


def main():
    T = int(input())
    result = []
    for i in range(T):
        count = solve()
        result.append(count)
    
    for r in result:
        print(r)

if __name__ ==  "__main__":
    main()