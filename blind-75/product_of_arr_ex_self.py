# leetcode 238

from typing import List

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:

		prefixArr = [1]

		for n in nums:
			prefixArr.append(prefixArr[-1] * n)

		postfixArr = [1]

		for n in nums[::-1]:
			postfixArr.append(postfixArr[-1] * n)

		postfixArr.reverse()

		res = []
		for i in range(len(prefixArr) - 1):
			res.append(prefixArr[i] * postfixArr[i + 1])


		return res



obj = Solution()

nums = [1,2,3,4]
print(obj.productExceptSelf(nums))


nums = [-1,1,0,-3,3]
print(obj.productExceptSelf(nums))
