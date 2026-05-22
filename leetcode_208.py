from typing import List
from typing import Optional
from typing import Dict

# class TreeNode:
#     def __init__(self, val: None, children: List):
        
#         self.val = val
#         self.children = children

# class Trie:
#     def __init__(self):
#         self.rootMap = dict()
    
#     def printTrie(self, node: Optional[TreeNode]) -> None:
#         if node:
#             print(f"parent: {node.val}, childLength: {len(node.children)}")
        
#             for child in node.children:
#                 print(f"node: {child.val}")
#                 self.printTrie(child)
    
#     # Helper method to insert data to TreeNode
#     def findAndInsert(self, word: str, depth: int, node: Optional[TreeNode]) -> TreeNode:
#         if node is None:
#             newNode = TreeNode(word[depth], [])
#             if depth + 1 < len(word):
#                 childNode = self.findAndInsert(word, depth + 1, None)
#                 if childNode:
#                     newNode.children.append(childNode)
#             return newNode

#         elif node.val == word[depth]:
#             if depth + 1 < len(word):
#                 for child in node.children:
#                     if child.val == word[depth + 1]:
#                         self.findAndInsert(word, depth + 1, child)
#                         return node
                
#                 # If no matching child found, create a new one
#                 childNode = self.findAndInsert(word, depth + 1, None)
#                 if childNode:
#                     node.children.append(childNode)
#             return node
                
            
    
#     # Helper method to search through the tree nodes and confirm the existent
#     def searchAndConfirm(self, word: str, depth: int, node: TreeNode) -> bool:
#         if depth < len(word):
#             # print(f"searching for {word[depth]} at depth {depth} in node {node.val}")
#             if depth + 1 < len(word):
#                 for child in node.children:
#                     if child.val == word[depth + 1]:
#                         return self.searchAndConfirm(word, depth + 1, child)

#                 return False
        
#         return True
        
#     # Data insertion
#     def insert(self, word: str) -> None:
#         word = word + "."
#         if self.rootMap.get(word[0]) is None:
#             self.rootMap[word[0]] = self.findAndInsert(word, 0, None)
#         else:
#             self.findAndInsert(word, 0, self.rootMap[word[0]])
        
#         # for k,v in self.rootMap.items():
#         #     self.printTrie(v)
    
#     # Data search
#     def search(self, word: str) -> bool:
#         if self.rootMap.get(word[0]) is None:
#             return False
        
#         word = word + "."
#         return self.searchAndConfirm(word, 0, self.rootMap[word[0]])
    
#     # Data search
#     def startsWith(self, prefix: str) -> bool:
#         if self.rootMap.get(prefix[0]) is None:
#             return False
        
#         return self.searchAndConfirm(prefix, 0, self.rootMap[prefix[0]])

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        currNode = self.root
        
        for ch in word:
            if ch in currNode.children:
                currNode = currNode.children[ch]
            else:
                currNode.children[ch] = TrieNode()
                currNode = currNode.children[ch]
        
        currNode.isWord = True
        
    
    def search(self, word: str) -> bool:
        def dfs(currNode: Optional[TrieNode], word: str, index: int) -> bool:
            if index < len(word):
                ch = word[index]
                if ch in currNode.children:
                    return dfs(currNode.children[ch], word, index + 1)
                else:
                    return False
            
            return currNode.isWord
        
        if word[0] not in self.root.children:
            return False
        return dfs(self.root, word, 0)

    def startsWith(self, prefix: str) -> bool:
        def dfs(currNode: Optional[TrieNode], prefix: str, index: int) -> bool:
            if index < len(prefix):
                ch = prefix[index]
                if ch in currNode.children:
                    return dfs(currNode.children[ch], prefix, index + 1)
                else:
                    return False
            
            return True
        
        if prefix[0] not in self.root.children:
            return False
        return dfs(self.root, prefix, 0)
        
        


obj = Trie()
word = "ape"
print(obj.search(word)) # False
print(obj.startsWith(word)) # False
obj.insert(word)
print(obj.search(word)) # True
word = "apple"
obj.insert(word)
print(obj.search(word)) # True
print(obj.search('app')) # False
print(obj.startsWith('app')) # True

word = "app"
obj.insert(word)
print(obj.search(word)) # True
