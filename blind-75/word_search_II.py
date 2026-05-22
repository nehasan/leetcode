# leetcode 212

from typing import List
from collections import defaultdict

class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

		def backtrackAndBuilWords(board, wordSet, visitSet, pos, curr) -> None:

			i, j = pos
			curr.append(board[i][j])
			wordSet.add("".join(curr))

			tempChar = board[i][j]
			board[i][j] = "#"

			for x, y in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
				dx, dy = i + x, j + y
				if 0 <= dx < len(board) and 0 <= dy < len(board[0]) and \
						board[dx][dy] != "#" and (dx, dy) not in visitSet:
					# visitSet.add((dx, dy))
					backtrackAndBuilWords(board, wordSet, visitSet, (dx, dy), curr)
					# visitSet.remove((dx, dy))

			board[i][j] = tempChar


		wordSet = set()
		visitSet = set()

		for i in range(len(board)):
			for j in range(len(board[0])):
				visitSet.clear()
				backtrackAndBuilWords(board, wordSet, visitSet, (i, j), [])

		print(wordSet)
		res = []
		for word in words:
			if word in wordSet:
				res.append(word)

		return res


obj = Solution()
board = [["a","b"],["c","d"]]
words = ["abcb"]
print(obj.findWords(board, words))
# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]
# print(obj.findWords(board, words))