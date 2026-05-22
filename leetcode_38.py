
from typing import List


class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         
        rowSize = len(board)
        colSize = len(board[0])
        
        print(f"rowSize: {rowSize}, colSize: {colSize}")
        
        def validInRowCol(num: int, rowPos, colPos) -> bool:
            print(f"rowPos: {rowPos}, colPos: {colPos}")
            h = dict()
            for m in range(colSize):
                print (f"current m: {m} current board val: {board[rowPos][m]}")
                
                if board[rowPos][m] != ".":
                    if h.get(board[rowPos][m]) != None:
                        return False
                    else:
                        h[board[rowPos][m]] = board[rowPos][m]
            
            if len(h) == 0: return False
            h.clear()
            
            for n in range (rowSize):
                print (f"current n: {n} current board val: {board[n][colPos]}")
                
                if board[n][colPos] != ".":
                    if h.get(board[n][colPos]) != None:
                        return False
                    else:
                        h[board[n][colPos]] = board[n][colPos]
            
            if len(h) == 0: return False        
            return True
        
        # Checking sub boxes
        positions = [[0, 0], [0, 3], [0, 6],
                     [3, 0], [3, 3], [3, 6],
                     [6, 0], [6, 3], [6, 6]]
        
        for p in positions:
            print(f"checking fpr position p: #{p}")
            hMap = dict()
            for i in range(p[0], p[0] + 3):
                for j in range(p[1], p[1] + 3):
                    if board[i][j] != ".":
                        if hMap.get(board[i][j]) != None:
							
                            print(f"returning false due to subbox violation! hMap: #{hMap}, curr val: #{board[i][j]}")
                            return False
                        else:
                            hMap[board[i][j]] = board[i][j]
        
        # Checking rows and columns
        for i in range(rowSize):
            for j in range(colSize):
                if validInRowCol(board[i][j], i, j) == False:
                    return False
        
        return True


'''
Testcase 1
Output: True
board = [["5","3",".",".","7",".",".",".","."]
		,["6",".",".","1","9","5",".",".","."]
		,[".","9","8",".",".",".",".","6","."]
		,["8",".",".",".","6",".",".",".","3"]
		,["4",".",".","8",".","3",".",".","1"]
		,["7",".",".",".","2",".",".",".","6"]
		,[".","6",".",".",".",".","2","8","."]
		,[".",".",".","4","1","9",".",".","5"]
		,[".",".",".",".","8",".",".","7","9"]]
'''

board = [["5","3",".",".","7",".",".",".","."]
		,["6",".",".","1","9","5",".",".","."]
		,[".","9","8",".",".",".",".","6","."]
		,["8",".",".",".","6",".",".",".","3"]
		,["4",".",".","8",".","3",".",".","1"]
		,["7",".",".",".","2",".",".",".","6"]
		,[".","6",".",".",".",".","2","8","."]
		,[".",".",".","4","1","9",".",".","5"]
		,[".",".",".",".","8",".",".","7","9"]]

# Testcase 2
# Output: False
'''
board = [["8","3",".",".","7",".",".",".","."]
		,["6",".",".","1","9","5",".",".","."]
		,[".","9","8",".",".",".",".","6","."]
		,["8",".",".",".","6",".",".",".","3"]
		,["4",".",".","8",".","3",".",".","1"]
		,["7",".",".",".","2",".",".",".","6"]
		,[".","6",".",".",".",".","2","8","."]
		,[".",".",".","4","1","9",".",".","5"]
		,[".",".",".",".","8",".",".","7","9"]]
'''

'''
Testcase 3
Output: False
board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
'''



soln = Solution()
print(soln.isValidSudoku(board))