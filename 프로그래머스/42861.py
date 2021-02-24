import heapq

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    pa = find_parent(a, parent)
    pb = find_parent(b, parent)
    
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

def solution(n, costs):
    answer = 0
    
    q = []
    
    for a, b, c in costs:
        heapq.heappush(q, (c, a, b))
        
    parent = []
    for i in range(n):
        parent.append(i)
    
    total = 0
    
    for i in range(len(costs)):
        c, a, b = heapq.heappop(q)
        
        fa = find_parent(a, parent)
        fb = find_parent(b, parent)
        #print(a, b, fa, fb)
        if fa == fb: # 연결된 것이므로 
            continue
        
        union_parent(a, b, parent)
        total += c
        
    answer = total
    
    return answer