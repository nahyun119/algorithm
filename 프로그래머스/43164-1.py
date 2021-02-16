# 원래 풀었던게 생각보다 시간이 오래걸려서
# dfs로 풀었는데 약 300ms 정도 감소함,, 그리고 메모리도₩!
# 다른 사람들 풀이보면 더 짧게 나오던데 다들 답이 다 똑같다..
# 흠,,,ㅠ 

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
    
    # 시간을 줄여보자 
    
    def dfs(node, course, ticket_list):
        if not ticket_list:
            result.append(course)
            return

        if node in hash_map:
            for end in hash_map[node]:
                if (node, end) in ticket_list:
                    new_tickets = ticket_list[:]
                    new_tickets.remove((node, end))
                    dfs(end, course + [end], new_tickets)
                
    dfs('ICN', ['ICN'], ticket_l)    
    
    result.sort()

    return result[0]
    