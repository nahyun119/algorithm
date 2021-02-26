import sys
input = sys.stdin.readline

def solve():
    grade_str = input().strip()
    grade_list = grade_str.split(' ')
    #print(grade_list)
    grade = [0] * (101)

    for g in grade_list:
        grade[int(g)] += 1
    
    max_value = max(grade)
    for i in range(100, -1, -1):
        if grade[i] == max_value:
            return i


def main():
    T = int(input())
    for _ in range(T):
        order = int(input())
        result = solve()
        print("#" + str(order),result)

if __name__ ==  "__main__":
    main()