# leetcode 46

from typing import List
from collections import deque

class Solution:

	def backtrack(self, nums: List[int], currNumbers: List[int], permutations: List[List[int]]):
		
		print(f"currNumber: {currNumbers}")

		if len(currNumbers) == len(nums):
			print(f"permutations: {permutations}")
			permutations.append(currNumbers.copy())

			return


		for n in nums:
			if n not in currNumbers:
				currNumbers.append(n)
				self.backtrack(nums, currNumbers, permutations)
				currNumbers.pop()

		return


	def permute(self, nums: List[int]) -> List[List[int]]:

		permutations = []
		self.backtrack(nums, [], permutations)
		return permutations


obj = Solution()
nums = [1,2,3]
print(obj.permute(nums))