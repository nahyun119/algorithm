## 16508 dfs로 푼거 


# def dfs(visited, word, value):
#     global min_value
    
#     if word == '':
#         if min_value > value:
#             min_value = value 
#         return 

#     for i in range(n):
#         if visited[i] == 0:
#             visited[i] = 1
#             price, name = q[i]
#             remain = ''
#             for w in word:
#                 if w not in name:
#                     remain += w 
#             dfs(visited, remain, value + price)
#             visited[i] = 0

# dfs(visited, W, 0)