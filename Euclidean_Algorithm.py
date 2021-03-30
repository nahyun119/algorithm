# 유클리드 호제법
a, b = map(int, input().split())

# q, r = divmod(a, b)
# divisor = r
# dividend = b

# while r != 0:
#     q, r = divmod(dividend, divisor)
#     # print(dividend, divisor, q, r)
#     dividend = divisor
#     divisor = r 

# print(dividend)

# 나누는 수가 다음 단계에서 나눠지는 수로 divisor -> dividend
# 나머지가 다음 단계에서 나누는 수로 r -> divisor
dividend = a
divisor = b

while divisor != 0:
    temp = dividend % divisor
    dividend = divisor
    divisor = temp

print(dividend)