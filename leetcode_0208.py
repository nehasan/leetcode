from collections import defaultdict

class TrieNode:
    def __init__(self, val = None):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        currNode = self.root
        
        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()
            
            currNode = currNode.children[c]
        
        currNode.isWord = True

    def search(self, word: str) -> bool:
        currNode = self.root
        
        for c in word:
            if c not in currNode.children:
                return False
            
            currNode = currNode.children[c]
        
        return currNode.isWord
        

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        
        for c in prefix:
            if c not in currNode.children:
                return False
            
            currNode = currNode.children[c]
        
        return True
        

obj = Trie()
obj.insert("apple")
print(obj.search("apple"))

def test_case_0001():
    obj.insert("apple")
    assert(obj.search("apple")) == True

def test_case_0002():
    # obj.insert("apple")
    assert(obj.search("app")) == False

def test_case_0003():
    assert(obj.startsWith("app")) == True

def test_case_0004():
    obj.insert("app")
    assert(obj.search("app")) == True

 