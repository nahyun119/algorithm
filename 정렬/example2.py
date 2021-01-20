def get_score(data):
    return data[1]

def main():
    N = int(input())

    students = []
    for i in range(N):
        name, score = map(str, input().split())
        students.append((name, int(score)))

    #students = sorted(students, key = get_score)
    # lambda를 이용한 경우
    students = sorted(students, key = lambda students: students[1])

    for name, score in students:
        print(name, end = ' ')

if __name__ ==  "__main__":
    main() 