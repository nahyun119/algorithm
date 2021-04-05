n, k = map(int, input().split())
k = str(k)

# 0을 고려하는 것을 잊지말자. 
count = 0 
for h in range(0, n + 1):
    for m in range(60):
        for s in range(60):
            if h < 10:
                hour = '0' + str(h)
            else:
                hour = str(h)

            if m < 10:
                minute = '0' + str(m)
            else:
                minute = str(m)

            if s < 10:
                second = '0' + str(s)
            else:
                second = str(s)
             
            # print(hour, minute, second) 
            if k in hour or k in minute or k in second:
                count += 1

print(count)