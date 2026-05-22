from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        currNode = self.root
        
        for alpha in word:
            if alpha not in currNode.children:
                currNode.children[alpha] = TrieNode()
                
            currNode = currNode.children[alpha]
        
        currNode.isWord = True

    def search(self, word: str) -> bool:
        
        def dfsSearch(currNode: TrieNode, word: str) -> bool:
            # print(f"currWord window: {word}")
            if word == "":
                return currNode.isWord
            
            alpha = word[0]
            if alpha == ".":
                for k,v in currNode.children.items():
                    if dfsSearch(v, word[1:]):
                        return True
            else:
                if alpha in currNode.children:
                    currNode = currNode.children[alpha]
                    return dfsSearch(currNode, word[1:])
            
            return False
        
        currNode = self.root
        return dfsSearch(currNode, word)
                
        



obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")

print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))
print(obj.search("c.."))