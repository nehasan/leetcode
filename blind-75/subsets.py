# leetcode 78

from typing import List

class Solution:

	'''
	Approach, recursive backtracking
	Initially the res tray will be empty. Now for each execution stack context
	we choose two paths:
	1) we do not select any numbers and
	2) select a number.
	However, this DFS go deep until it hits the index == len(nums), we put the solution
	to the result tray just right then.
	When the exection stack gets back to it previous stack then we remove the last inserted
	number from the current numbers tray
	'''
	def backtrack(self, nums, res, sol, index) -> None:
		if index == len(nums):
			res.append(sol.copy())
			return

		
		# do not select any numbers
		self.backtrack(nums, res, sol, index + 1)
		sol.append(nums[index])
		self.backtrack(nums, res, sol, index + 1)
		sol.pop()



	def subsets(self, nums: List[int]) -> List[List[int]]:
		
		res = []
		sol = []
		self.backtrack(nums, res, sol, 0)

		return res


obj = Solution()
print(obj.subsets([1,2,3]))