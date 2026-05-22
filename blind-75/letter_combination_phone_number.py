# leetcode 17

from typing import List

class Solution:

	'''
	Same approach for leetcode "Subsets" problem. Used backtracking to add the letters
	and letter poped out the letters in the decision tree.
	'''
	def findCombinations(self, digits: str, digitToLettersDict: dict, res: List[str], sol: List[str], index: int) -> None:
		if index == len(digits):
			res.append("".join(sol))
			return

		for letter in digitToLettersDict[digits[index]]:
			# print(letter)
			sol.append(letter)
			self.findCombinations(digits, digitToLettersDict, res, sol, index + 1)
			sol.pop()



	def letterCombinations(self, digits: str) -> List[str]:

		if digits == "":
			return []

		res, sol = [], []

		digitToLettersDict = {
			'2': "abc", '3': "def", '4': "ghi", '5': "jkl", 
			'6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
		}


		self.findCombinations(digits, digitToLettersDict, res, sol, 0)

		return res


obj = Solution()

digits = "23"
print(obj.letterCombinations(digits))

digits = "232"
print(obj.letterCombinations(digits))