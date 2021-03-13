# 대량의 소수를 구하기때문에 에라토스테네스의 체를 사용한다!! 
numbers = []
while True:
    n = int(input())
    if n == 0:
        break 
    numbers.append(n)

max_value = (max(numbers) * 2 + 1)
sieve = [True] * max_value
# 제일 큰 수를 이용해서 한번만 소수를 구한다. 
m = int(max_value ** 0.5) # n의 최대 약수는 sqrt(n) 이하 이므로 sqrt(n) 이하까지 검사 
for i in range(2, m + 1):
    if sieve[i] == True: # i가 소수인 경우 
        for j in range(i + i, max_value, i): # i의 배수를 삭제 
            sieve[j] = False 


for i in numbers:
    temp = [x for x in range(i + 1, i * 2 + 1) if sieve[x] == True]
    #print(temp)
    print(len(temp))



    
