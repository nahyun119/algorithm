import sys
input = sys.stdin.readline 

def main():
    sys.setrecursionlimit(10 ** 7)
    gear = []

    for _ in range(4):
        g = str(input().strip())
        gear.append(list(g))
    
    k = int(input())

    def clockwise(number): # 시계방향 회전 
        temp = gear[number][7]
        gear[number] = [temp] + gear[number][:7]
    
    def counter_clockwise(number): # 시계 반대 방향 회전 
        temp = gear[number][0] 
        gear[number] = gear[number][1: ] + [temp] # 맨 처음 톱니바퀴가 맨 마지막으로

    def rotate_right(index, direc): # 오른쪽으로 계속 회전할 수 있는지 확인 
        if index > 3: # 범위를 벗어나면 return 
            return 
        if gear[index - 1][2] == gear[index][6]: # 자신이 돌아갈 수 있는지 자신의 왼쪽의 극을 확인, 극이 일치해서 돌아갈 수 없으므로 
            return 
        else:
            rotate_right(index + 1, (-1) * direc)
            if direc == 1:
                clockwise(index)
            else:
                counter_clockwise(index)
    
    def rotate_left(index, direc):
        if index < 0 :
            return 
        if gear[index + 1][6] == gear[index][2]: # 왼쪽으로 돌아갈 수 있는지 확인하기 위해서 나의 오른쪽 톱니바퀴를 확인 
            return
        else:
            rotate_left(index - 1, (-1) * direc)
            if direc == 1:
                clockwise(index)
            else:
                counter_clockwise(index)

    for _ in range(k):
        number, direc = map(int, input().split())
        rotate_left(number - 2,(-1) * direc)
        rotate_right(number, (-1) * direc)
        if direc == 1:
            clockwise(number - 1)
        else:
            counter_clockwise(number - 1)

        # for i in range(4):
        #     print(str(gear[i]))
    
    answer = 0
    for i in range(4):
        #print(str(gear[i]))
        if gear[i][0] == '1':
            answer += (2 ** i)
    print(answer)



if __name__ ==  "__main__":
    main()