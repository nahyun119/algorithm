# 프로그래머스 코딩테스트 연습 첫번째 문제 (체육복)

# 경우의 수를 따져보면 된다
# lost reserve
#  o      o    => 자기만 입을 수 있다. 
#  o      x    => 빌려야한다. 대신 빌릴 때 lost에는 없고 reserve에만 있는 학생으로(lost와 reserve에 모두있는 학생은 빌려줄 수 없다)
#  x      o    => 빌려줄 수 있다.
#  x      x    => 자기 체육복이 있으므로 자기만 입을 수 있다. 

def solution(n, lost, reserve):
    answer = 0
    
    count = 0 
    for value in range(1, n+1):
        if(value in lost and value not in reserve):
            if(value - 1 in reserve and value - 1 not in lost):
                reserve.remove(value - 1)
                count += 1
            else: 
                if(value + 1 in reserve and value + 1 not in lost):
                    reserve.remove(value + 1)
                    count += 1
        else:
            count += 1
    
    return count