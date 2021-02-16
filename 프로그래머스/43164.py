from collections import deque

# 항공권이 중복이 될 수 있다... -> 매우 중요!!!!

def solution(tickets):
    answer = []
    
    hash_map = {}
    ticket_l = []
    
    for ticket in tickets:
        start, end = ticket[0], ticket[1]
        ticket_l.append((start, end))
        if start in hash_map:
            hash_map[start].append(end)
        else:
            hash_map[start] = [end]
        
    result = []
    
    q = deque()
    q.append(('ICN', ticket_l, ['ICN']))
    
    while q:
        node, ticket_list, course = q.popleft()
        #print(node, ticket_list, course)
        if len(ticket_list) == 0:
            result.append(course)
            #break
        
        if node in hash_map:
            for end in hash_map[node]:
                if (node, end) in ticket_list: # 항공권이 중복이 될 수있다.
                    new_course = course[:]
                    new_course.append(end)
                    new_tickets = ticket_list[:]
                    new_tickets.remove((node, end))
                    q.append((end, new_tickets, new_course))
        else:
            continue
    
    result.sort()
    return result[0]
    