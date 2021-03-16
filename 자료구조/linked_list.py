class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        dummy = Node("dummy") # 더미 노드 생성 
        self.head = dummy # 맨 앞 노드 
        self.tail = dummy # 맨 끝 노드 

        self.current = None # 현재 위치 
        self.before = None # 현재 위치 전 

        self.size = 0 # 리스트 크기(노드 수)

    def append(self, data): # 노드 삽입 
        new_node = Node(data)
        self.tail.next = new_node # 현재 맨 끝 노드의 다음 노드를 새로운 노드로 업데이트 
        self.tail = new_node # 현재 맨 끝 노드를 새로운 노드로 업데이트 

        self.size += 1 # 크기를 늘려준다
    
    def delete(self): # 노드 삭제 
        pop_data = self.current.data # 현재 위치 데이터를 가져온다.

        if self.current is self.tail: # 현재 위치가 제일 끝 노드라면 
            self.tail = self.before # 현재 위치 전의 노드가 제일 끝 노드가 된다.
        
        self.before.next = self.current.next # 현재 위치 노드의 다음 노드를 현재 위치 전의 다음 노드로 수정 
        self.current = self.before # 현재 위치를 현재 위치 전 노드로 수정 

        self.size -= 1 # 사이즈 감소 
    
    def first(self): # 맨 앞 노드 검색(head 이후의 맨 앞 노드)
        if self.size == 0: # 데이터가 없는 경우
            return None # 첫번째 노드가 없다.
        
        self.before = self.head # 현재 위치 전을 제일 맨 앞 노드로 
        self.current = self.head.next # 현재 위치를 제일 맨 앞 노드의 다음 노드로 수정 

        return self.current.data 
    
    def next(self): # 다음 노드 검색 
        if self.current.next == None: # 다음 노드가 없는 경우 None을 반환 
            return None 
        
        self.before = self.current # 현재 위치 전 노드를 현재 위치로 업데이트 
        self.current = self.current.next # 현재 위치를 현재 위치의 다음 노드로 업데이트 

        return self.current.data 

    def get_size(self):
        return self.size # 크기 


l_list = LinkedList() # 링크드 리스트 생성 
l_list.append(5) # 데이터 삽입 
l_list.append(2)
l_list.append(1)
l_list.append(2)
l_list.append(7)
l_list.append(2)
l_list.append(11)

print(l_list.current, l_list.before, l_list.head.data, l_list.tail.data)  # 맨 처음 None, None, dummy, 11(제일 마지막에 삽입된 노드)
print(l_list.head.next.data) # head 다음 노드는 제일 먼저 삽입된 노드 
print('first :', l_list.first())  # == l_list.head.next.data   
print('next :', l_list.next()) # 현재 위치가 first 이므로 first 다음 노드     
print('size :', l_list.get_size())    # 크기    
print('delete :', l_list.delete())    # delete 한 후 
print('size :', l_list.get_size())    # 크기가 감소했음을 알 수 있다.  
print('current:', l_list.current.data)
#   print('tail:', l_list.tail.data)      
#   print('first :', l_list.first())      
#   print('next :', l_list.next())      
#   print('next :', l_list.next())       
#   print('next :', l_list.next())    

## first 부터 차례차례 next를 하면서 다음 노드로 이동하면서 탐색할 수 있다. 
## 원하는 데이터를 삭제하는 경우에도 처음부터 next를 이용하여 이동하면서 데이터를 비교하여 삭제할 수 있다. 
