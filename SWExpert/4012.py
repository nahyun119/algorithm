from collections import deque

T = int(input())
for t in range(T):
    n = int(input())
    food = []
    for i in range(n):
        food.append(list(map(int, input().split())))
    
    q = deque()

    hash_map = {}

    for i in range(n):
        q.append((0, [i]))
    
    min_value = 1e9
    while q:
        value, node = q.popleft()
        if len(node) >= n // 2:
            a = []
            for i in range(n):
                if i not in node:
                    a.append(i)
            a_node = tuple(a)
            t_node = tuple(node)

            if a_node in hash_map:
                v = abs(hash_map[a_node] - value)
                if v < min_value:
                    min_value = v 
            else:
                hash_map[t_node] = value
            continue

        for i in range(node[-1] + 1, n):
            new_node = node + [i]
            v = 0
            for j in node:
                v += food[i][j] + food[j][i]
            q.append((value + v, new_node))

    print("#" + str(t + 1), min_value)
   
    
    