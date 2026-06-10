from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -10001
        currSum = 0

        for n in nums:
            currSum = max(currSum + n, n)
            maxSum = max(maxSum, currSum)
        
        return maxSum


soln = Solution()
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
nums = [-1]
print(soln.maxSubArray(nums))