from collections import deque
for t in range(10):
    n, start = map(int, input().split())
    temp = list(map(int, input().split()))
    hash_map = {}

    for i in range(0, n, 2):
        a, b = temp[i], temp[i + 1]
        if a in hash_map:
            hash_map[a].append(b)
        else:
            hash_map[a] = [b]
    
    visited = []
    v = []
    
    q = deque()
    q.append((start, 0))
    
    v.append([start])
    visited.append(start)

    while q:
        node, step = q.popleft()
        #print(visited)
        if node in hash_map:
            for i in hash_map[node]:
                if i not in visited:
                    q.append((i, step + 1))
                    visited.append(i)
                    if len(v) <= step + 1:
                        v.append([i])
                    elif len(v) == step + 2:
                        v[step + 1].append(i)

        else:
            continue
   
    print("#" + str(t + 1), max(v[-1]))