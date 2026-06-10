import sys
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstLowest = sys.maxsize
        secondLowest = sys.maxsize

        for n in nums:
            if n < firstLowest:
                firstLowest = n
            elif n < secondLowest:
                secondLowest = n
            else:
                return True
                        
        
        return False


soln = Solution()
# nums = [0,4,2,1,0,-1,-3]
# nums = [20,100,10,12,5,13]
# nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
nums = [1,1,1,1,1]
print(soln.increasingTriplet(nums))