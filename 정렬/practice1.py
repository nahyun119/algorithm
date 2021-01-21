def main():
    N = int(input())

    students = []
    for i in range(N):
        name, l, m, e = map(str, input().split())
        students.append((name, int(l), int(m), int(e)))
    
    # 이런 식으로 lambda를 이용해서 기준을 정하고 오름차순, 내림차순 정렬할지를 정할 수 있다.
    # 기억해둘것!
    students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0])) 

    for student in students:
        print(student[0])

if __name__ ==  "__main__":
    main() 