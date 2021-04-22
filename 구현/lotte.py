k = int(input())

def change(number):
    temp = ""
    for i in number:
        if i == "0":
            temp += "1"
        elif i == "1":
            temp += "0"
    return temp

number = "0"
for i in range(2, k + 1):
    front = number
    back = change(number)
    number = front + back
    if len(number) >= k:
        print(number[k - 1])
        break 