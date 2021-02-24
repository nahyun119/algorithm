import sys
import heapq
input = sys.stdin.readline


result = []
def check(value, q):
    global result
    temp = []
    heapq.heappush(temp, value[1])

    while q:
        node = heapq.heappop(q)
        if value[0] != node[0]:
            heapq.heappush(q, node)
            break 
        else:
            heapq.heappush(temp, node[1])

    v = heapq.heappop(temp)

    result.append(v)

    for r in temp:
        heapq.heappush(q, (abs(r), r))
    
    return q
    



def main():
    n = int(input())

    q = []
    global result

    for _ in range(n):
        #print(q)
        o = int(input())
        if o == 0:
            if q:
                node = heapq.heappop(q)
                q = check(node, q)
            else:
                result.append(0)
        else:
            heapq.heappush(q, (abs(o), o))

    for r in result:
        print(r)

if __name__ ==  "__main__":
    main()