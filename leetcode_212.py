from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordMap = dict()
        r = len(board)
        c = len(board[0])
        visited = []
        
        for i in range(r):
            for j in range(c):
                if wordMap.get(board[i][j]) is None:
                    wordMap[board[i][j]] = [[i, j]]
                else:
                    wordMap[board[i][j]].append([i, j])
        
        
        def DFS(pos: List[int], r: int, c: int, curr: int, word: str, board: List[List[str]], visited: List[List[int]], parentPos: List[int]) -> bool:
            if curr >= len(word):
                return True
            
            # print(f'pos[0]: {pos[0]}, pos[1]: {pos[1]}')
            if pos[0] >= 0 and pos[0] < r and pos[1] >= 0 and pos[1] < c:
                
                print(f"pos0:{pos[0]}, pos1: {pos[1]}, board: {board[pos[0]][pos[1]]}, visited: {visited}")
                # if curr >= len(word):
#                     return True
                
                if board[pos[0]][pos[1]] == word[curr]:
                    # print('here')
                    left  = False
                    up    = False
                    right = False
                    down  = False
                    visited.append(pos)
                    
                    if [pos[0], pos[1] - 1] not in visited:
                        left = DFS([pos[0], pos[1] - 1], r, c, curr + 1, word, board, visited, pos) # left adjecent
                    
                    if [pos[0] - 1, pos[1]] not in visited:
                        up = DFS([pos[0] - 1, pos[1]], r, c, curr + 1, word, board, visited, pos) # up adjecent
                    
                    if [pos[0], pos[1] + 1] not in visited:
                        right = DFS([pos[0], pos[1] + 1], r, c, curr + 1, word, board, visited, pos) # right adjecent
                    
                    if [pos[0] + 1, pos[1]] not in visited:
                        down = DFS([pos[0] + 1, pos[1]], r, c, curr + 1, word, board, visited, pos) # left adjecent
                    
                    if left == False and up == False and right == False and down == False:
                        visited.pop()    
                    return True and (left or up or right or down)
            
            return False
                    
                
        res = []

        # print(wordMap)
        for word in words:
            wordFound = False
            
            if wordMap.get(word[0]) is not None:
                wordFound = True
                positions = wordMap[word[0]]
                for pos in positions:
                    print(f"Searching for word: {word} starting at pos: {pos}")
                    visited = []
                    wordFound = DFS(pos, r, c, 0, word, board, visited, [])
                    print(wordFound)
                    
                    if wordFound == True:
                        break
            
            if wordFound == True:
                res.append(word)
            
        return res

soln = Solution()
# board = [['a', 'b'], ['c', 'd']]
# words = ['abcd']

# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]

# board = [["a"]]
# words = ["a"]

# board = [["a", "a"]]
# words = ["aaa"]

# board = [["a","b"],["a","a"]]
# words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
# words = ["aaba"]

board = [["a","b","c"],["a","e","d"],["a","f","g"]]
# words = ["gfedcbaaa","eaabcdgfa"]
words = ["eaafgdcba","eaabcdgfa"]

# board = [["a","a","x","x"],["a","a","y","y"]]
# words = ["aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa"]
print(soln.findWords(board, words))