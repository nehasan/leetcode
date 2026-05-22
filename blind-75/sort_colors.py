# leetcode 75

from typing import List
from collections import defaultdict

class Solution:

	'''
	Approach using map, counting total number of different colors
	Then just overwrite the number of colors into 'nums' variable
	'''
	def sortColors(self, nums: List[int]) -> None:
		"""
    Do not return anything, modify nums in-place instead.
    """
		
		numCounts = defaultdict(int)

		for n in nums:
			numCounts[n] += 1

		index = 0
		for color in [0,1,2]:
			counts = numCounts[color]
			while counts > 0:
				nums[index] = color
				counts -= 1
				index += 1

		# print(nums)


obj = Solution()

nums = [2,0,2,1,1,0]
obj.sortColors(nums)

nums = [2,0,1]
obj.sortColors(nums)