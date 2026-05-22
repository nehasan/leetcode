from typing import Dict

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.isWord: bool = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        currNode = self.root
        for ch in word:
            if ch in currNode.children:
                currNode = currNode.children[ch]
            else:
                currNode.children[ch] = TrieNode()
                currNode = currNode.children[ch]
        currNode.isWord = True
    
    def search(self, word: str) -> bool:
        def dfs(currNode: TrieNode, word: str, index: int) -> bool:
            if index < len(word):
                ch = word[index]
                if ch == '.':
                    for k, child in currNode.children.items():
                        if dfs(child, word, index + 1):
                            return True
                    return False
                elif ch in currNode.children:
                    currNode = currNode.children[ch]
                    return dfs(currNode, word, index + 1)
                else:
                    return False
                
            return currNode.isWord
        
        return dfs(self.root, word, 0)


obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad")) # False
# print(obj.search("bad")) # True
# print(obj.search(".ad")) # True
# print(obj.search("..d")) # True
# print(obj.search("b..")) # True

# obj.addWord("a")
# obj.addWord("ab")
# print(obj.search("a")) # True
# print(obj.search("a.")) # True
# print(obj.search("ab")) # True
# print(obj.search(".a")) # False
# print(obj.search(".b")) # True
# print(obj.search("ab.")) # False
# print(obj.search(".")) # True
# print(obj.search("..")) # True

obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
print(obj.search("a")) # False
print(obj.search(".at")) # False
obj.addWord("bat")
print(obj.search(".at")) # True
print(obj.search("an.")) # True
print(obj.search("a.d.")) # False
print(obj.search("b.")) # False
print(obj.search("a.d")) # True
print(obj.search(".")) # False