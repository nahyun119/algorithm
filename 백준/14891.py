import sys
input = sys.stdin.readline

## deque에서 rotate 기능이 있다. 
## 1이면 시계방향으로 움직이고, -1이면 시계반대방향으로 움직인다. 

## 왼쪽 오른쪽 순서대로 인접한 톱니바퀴가 움직일 수 있는지 확인해야한다. -> 14891-1.py


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

    def rotate(number, direc, pre): # 회전 시키는 함수 
        if number < pre: # 다시 회전할 수 없으므로 
            return 
        if number == 1: #1번 톱니바퀴는 2번만 고려 
            if direc == 1:
                if gear[number - 1][2] != gear[number][6]: # 극이 다르다면 회전할 수 있다. 
                    # counter_clockwise(number) # 1번이 시계방향 회전하면 2번은 반시계방향 회전
                    clockwise(number - 1) # 1번이 시계방향 회전 
                    rotate(number, (-1) * direc, number - 1) # 돌아가고나서 2번이 또 돌아갈 수 있는지 확인 
                else:
                    clockwise(number - 1) # 1번이 시계방향 회전
            else:
                if gear[number - 1][2] != gear[number][6]: # 극이 다르다면 회전할 수 있다. 
                    counter_clockwise(number - 1)   
                    rotate(number, (-1) * direcm, number - 1)
                    #clockwise(number) # 2번은 시계방향 회전
                else:
                    counter_clockwise(number - 1)   

        elif number == 4: # 4번 톱니바퀴는 3번만 고려 
            if direc == 1: # 시계방향 회전 
                if gear[number - 1][6] != gear[number - 2][2]:
                    clockwise(number - 1)
                    rotate(number - 2,  (-1) * direc, number - 1)
                    #counter_clockwise(number - 2)
                else:
                    clockwise(number - 1)
            else: # 반시계 방향 회전 
                if gear[number - 1][6] != gear[number - 2][2]:
                    counter_clockwise(number - 1)
                    rotate(number - 2,  (-1) * direc, number - 1)
                    #clockwise(number - 2)
                else:
                    counter_clockwise(number - 1)
        else:
            if direc == 1: # 시계방향 회전 
                if gear[number - 1][6] != gear[number - 2][2]:
                    clockwise(number - 1)
                    rotate(number - 2,  (-1) * direc, number - 1)
                    return 
                    #counter_clockwise(number - 2)
                else:
                    clockwise(number - 1)
                    return 
                if gear[number - 1][2] != gear[number][6]:
                    clockwise(number - 1)
                    rotate(number,  (-1) * direc, number - 1)
                    return 
                    #counter_clockwise(number)
                else:
                    clockwise(number - 1)
                    return 
            else: # 반시계방향 회전 
                if gear[number - 1][6] != gear[number - 2][2]:
                    counter_clockwise(number - 1)
                    rotate(number - 2,  (-1) * direc, number - 1)
                    return 
                    #clockwise(number - 2)
                else:
                    counter_clockwise(number - 1)
                    return 
                if gear[number - 1][2] != gear[number][6]:
                    counter_clockwise(number - 1)
                    rotate(number,  (-1) * direc, number - 1)
                    return 
                    #clockwise(number)
                else:
                    counter_clockwise(number - 1)
                    return 


    for _ in range(k):
        number, direc = map(int, input().split())
        rotate(number, direc, -1)
        for i in range(4):
            print(str(gear[i]))
    
    answer = 0
    for i in range(4):
        print(str(gear[i]))
        if gear[i][0] == '1':
            answer += (2 ** i)
    print(answer)
        

if __name__ ==  "__main__":
    main()