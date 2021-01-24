# 피보나치 수열을 재귀적으로 dp 방법 이용
# 반복해서 계산하는 것을 막기 위해 계산을 진행한 경우 배열에 값을 넣어서 저장한다.
# 그래서 다시 같은 계산을 해야하는 경우, 계산을 진행하지 않고 저장된 값을 가져와서 사용한다. -> 연산 횟수가 줄어든다. 
# Top down 방식 
d = [0] * 100 

def fibo(x):
    global d
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0: # 이미 fibo(x)를 진행한 경우 
        return d[x]
    else: # 계산을 하지 않은 경우 계산을 진행 
        d[x] = fibo(x - 1) + fibo(x - 2)
        return d[x]



def main():
    print(fibo(99))


if __name__ ==  "__main__":
    main()