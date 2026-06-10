from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = dict()

        for n in nums:
            if map.get(n) is None:
                map[n] = n
            else:
                return True
        
        return False


soln = Solution()
# nums = [1,2,3,1]
nums = [1,2,3,4]
print(soln.containsDuplicate(nums))