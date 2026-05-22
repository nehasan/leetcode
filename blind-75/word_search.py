# leetcode 79

from typing import List

class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:

		'''
		Approach using dfs backtracking.
		For each cell in the board we start searching the word from there. In the search path
		we put # if we find a valid letter. However after an invalid path we backtrack the # with the
		original character. Finally if we find that wordIndex is equal to the word length then we mark the path is true.
		Else always false
		Time complexity: O(m*n)**2
		Space complexity: O(m*n)
		'''
		def backtrack(board: List[List[str]], word, i, j, rowSize, colSize, wordIndex):
			if wordIndex == len(word):
					return True

			if board[i][j] != word[wordIndex]:
				return False

			tempChar = board[i][j]
			board[i][j] = "#"

			for x, y in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
				dx, dy = (i + x), (j + y)
				if 0 <= dx < rowSize and 0 <= dy < colSize:
					if backtrack(board, word, dx, dy, rowSize, colSize, wordIndex + 1) == True:
						return True

			board[i][j] = tempChar
			return False

		
		rowSize = len(board)
		colSize = len(board[0])

		if rowSize == 1 and colSize == 1:
			if board[0][0] == word:
				return True

		for i in range(rowSize):
			for j in range(colSize):
				if backtrack(board, word, i, j, rowSize, colSize, 0) == True:
						return True
					

		return False



obj = Solution()

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# print(obj.exist(board, word))


# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"
# print(obj.exist(board, word))


# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"
# print(obj.exist(board, word))

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print(obj.exist(board, word))

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
print(obj.exist(board, word))