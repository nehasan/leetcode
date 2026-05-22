# leetcode 39

from typing import List

class Solution:

	def backtrack(self, candidates: List[int], target: int, index: int, currNumbers: List[int], combinations: List[List[int]]) -> List[List[int]]:
		if target <= 0:
			if target == 0:
				combinations.append(currNumbers)

			return

		if index < len(candidates):
			value = candidates[index]
			currNumbers.append(value)
			self.backtrack(candidates, target - value, index, currNumbers.copy(), combinations)
			currNumbers.pop()
			self.backtrack(candidates, target, index + 1, currNumbers, combinations)

		# print(combinations)
		return combinations


	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		currNumbers = []
		combinations = []
		self.backtrack(candidates, target, 0, currNumbers, combinations)

		return combinations


obj = Solution()
candidates = [2,3,6,7]
target = 7
print(obj.combinationSum(candidates, target))


candidates = [2,3,5]
target = 8
print(obj.combinationSum(candidates, target))