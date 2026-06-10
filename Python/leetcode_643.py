import sys
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = - float(sys.maxsize)
        currTotal = 0.00000
        lastPos = 0

        for i in range(k):
            currTotal += nums[i]

        maxAvg = max(currTotal/k, maxAvg)

        for i in range(k, len(nums)):
            currTotal = (currTotal + nums[i]) - nums[lastPos]
            maxAvg = max(currTotal/k, maxAvg)
            lastPos += 1
        
        return maxAvg


soln = Solution()
nums = [-1]
k = 1
print(soln.findMaxAverage(nums, k))