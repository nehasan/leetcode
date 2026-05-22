# leetcode 419

from typing import List


class Solution:

	def floodFillTheBoard(self, board: List[List[str]], i: int, j: int, rowSize: int, colSize: int) -> None:
		if (i >= 0 and i < rowSize) and (j >= 0 and j < colSize) and board[i][j] == "X":
			board[i][j] = "O"

			self.floodFillTheBoard(board, i, j - 1, rowSize, colSize)
			self.floodFillTheBoard(board, i - 1, j, rowSize, colSize)
			self.floodFillTheBoard(board, i, j + 1, rowSize, colSize)
			self.floodFillTheBoard(board, i + 1, j, rowSize, colSize)

	def countBattleships(self, board: List[List[str]]) -> int:
		rowSize = len(board)
		colSize = len(board[0])
		totalBattleships = 0

		for i in range(rowSize):
			for j in range(colSize):
				if board[i][j] == 'X':
					totalBattleships += 1;
					self.floodFillTheBoard(board, i, j, rowSize, colSize)


		return totalBattleships



obj = Solution()

def test__001():
	board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
	assert(obj.countBattleships(board)) == 2

def test__002():
	board = [["."]]
	assert(obj.countBattleships(board)) == 0