class Node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {} # 자식 노드를 담는 map

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string): # 문자열 삽입 
        current = self.head 
        for char in string: # 문자별로 넣는다.
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]
        
        current.data = string # 맨 마지막 노드에 문자열을 넣는다. 
    
    def search(self, string): # 문자열 검색
        current = self.head
        for char in string:
            if char in current.children:
                current = current.children[char] # 문자가 있으면 그 문자로 업데이트해서 하위로 이동할 수 있도록 
            else:
                return False # 문자열이 없으므로 

        if current.data != None: # 데이터가 빈 경우 데이터가 있어야 해당 문자열이 trie에 있다는 의미이므로 
            return True 
        
        return False 

trie = Trie()
trie.insert("bear")
trie.insert("bell")
trie.insert("bid")
trie.insert("bull")

trie.insert("sell")
trie.insert("stock")
trie.insert("stop")

print(trie.search("bear"))
print(trie.search("bea"))



