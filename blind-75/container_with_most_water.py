# leetcode 11

from typing import List

class Solution:
	'''
	Approach: Two pointers.
	Area = width * height
	Area = (highIndex - lowIndex) * min of (height[low], hieght[high])
	Now we need to move the pointers towards each other
	If any of the height is lower than other then the lower height pointer move forward to
	the higher height pointer
	'''
	def maxArea(self, height: List[int]) -> int:

		maximumArea = -float('inf')

		low, high = 0, len(height) - 1

		while low < high:

			maximumArea = max(maximumArea, ((high - low) * min(height[low], height[high])))

			if height[low] < height[high]:
				low += 1
			elif height[low] > height[high]:
				high -= 1
			else:
				low += 1
				high -= 1

		return maximumArea



obj = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(obj.maxArea(height))

height = [1,1]
print(obj.maxArea(height))